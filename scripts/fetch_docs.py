# -*- coding: utf-8 -*-
"""
抓取 Vue3 / React / vue-router / Pinia 中文文档 → data/ 下平铺的 .md 语料文件。
VitePress 站点走官方 .md 端点（无损），React 走 HTML 正文提取（链接爬取）。
用法: python scripts/fetch_docs.py test   # 抓 1 页预览提取质量
      python scripts/fetch_docs.py go     # 全量抓取（已存在的文件跳过）
"""
import os, re, sys, time
import urllib.request
from html.parser import HTMLParser

sys.stdout.reconfigure(encoding="utf-8")  # Windows GBK 控制台防崩

OUT_DIR = r"d:\WLY_coding\agentic-rag\data"
DELAY = 0.25
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

SITES = [
    {"name": "vue", "base": "https://cn.vuejs.org", "md": True,
     "keep": ("/guide/", "/api/", "/tutorial/", "/style-guide/", "/about/faq.html")},
    {"name": "react", "base": "https://zh-hans.react.dev", "md": False,
     "keep": ("/learn/", "/reference/"), "crawl": ["/learn", "/reference/react"]},
    {"name": "vue_router", "base": "https://router.vuejs.org", "md": True,
     "keep": ("/zh/guide/", "/zh/api/")},
]

def fetch(url, tries=2):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=25) as r:
                return r.read().decode("utf-8", errors="replace")
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(1.5)

def clean_vue_md(md):
    """VitePress 原始 md → 纯文本 markdown"""
    lines = md.split("\n")
    if lines and lines[0].strip() == "---":
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), 1)
        lines = lines[end + 1:]
    out = []
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith("Are you an LLM?"):
            continue
        if s.startswith(":::") or s == ":::":
            continue  # VitePress 提示块标记
        s = re.sub(r"\{#[^}]*\}", "", s)            # 标题锚点 {#xxx}
        s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)  # 链接 → 文本
        s = re.sub(r"<[^>]+>", "", s)               # 残留 HTML 标签
        s = s.replace("**", "").replace("`", "")    # 加粗/行内代码标记
        out.append(s)
    md = "\n".join(out)
    return re.sub(r"[​‌‍﻿]", "", md)  # 零宽字符

def extract_main(html):
    """HTML → 正文片段。候选链：vp-doc → article → main → body(剥导航脚本)。
    每级提取都便宜、都可能失败（属性含 > 会骗过正则），所以按顺序取第一个
    长度 ≥ 500 的候选，坏的就丢掉——先到先得，不追求一次抠准。"""
    html = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", "", html, flags=re.S | re.I)
    frags = []
    m = re.search(r'<div class="vp-doc"[^>]*>', html)
    if m:
        i = m.end(); depth = 1
        for mm in re.finditer(r'<div\b[^>]*>|</div>', html[i:]):
            depth += -1 if mm.group(0).startswith("</") else 1
            if depth == 0:
                frags.append(html[m.start():mm.end() + i])
                break
        else:
            frags.append(html[m.start():])
    m = re.search(r"<article\b[^>]*>", html)
    if m:
        frags.append(re.split(r"</article>", html[m.start():], 1)[0])
    m = re.search(r"<main\b[^>]*>", html)
    if m:
        frags.append(re.split(r"</main>", html[m.start():], 1)[0])
    body = re.sub(r"<(nav|aside|header|footer)\b[^>]*>.*?</\1>",
                  "", html, flags=re.S | re.I)
    frags.append(body)
    for f in frags:
        if len(f) >= 500:
            return f
    return frags[-1]

class MDifier(HTMLParser):
    """正文片段 → 极简 markdown。只保内容，结构噪声可容忍。"""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.buf = ""
        self.in_pre = False

    def handle_starttag(self, tag, attrs):
        if tag == "pre":
            self.in_pre = True
            self.out.append("```")
        elif not self.in_pre and (tag in ("h1", "h2", "h3", "h4")
                                  or tag in ("p", "li", "blockquote", "tr", "td", "th")):
            self.buf = self.buf.strip()
            if self.buf:
                self.out.append(self.buf)
            self.buf = ""
        elif tag == "br" and not self.in_pre:
            self.buf += "\n"

    def handle_endtag(self, tag):
        if tag == "pre":
            self.out.append(self.buf.strip("\n"))
            self.out.append("```")
            self.buf = ""
            self.in_pre = False
        elif not self.in_pre and tag in ("h1", "h2", "h3", "h4"):
            self.out.append("#" * int(tag[1]) + " " + self.buf.strip())
            self.buf = ""
        elif not self.in_pre and tag == "p":
            if self.buf.strip():
                self.out.append(self.buf.strip())
            self.buf = ""
        elif not self.in_pre and tag == "li":
            if self.buf.strip():
                self.out.append("- " + self.buf.strip())
            self.buf = ""
        elif not self.in_pre and tag == "blockquote":
            if self.buf.strip():
                self.out.append("> " + self.buf.strip())
            self.buf = ""
        elif not self.in_pre and tag in ("td", "th"):
            if self.buf.strip():
                self.out.append(self.buf.strip() + " |")
            self.buf = ""

    def handle_data(self, data):
        self.buf += data

    def text(self):
        lines = [l.rstrip() for l in self.out if l.strip()]
        md = "\n".join(lines)
        return re.sub(r"[​‌‍﻿]", "", md)  # 零宽字符

def cjk_ratio(text):
    if not text:
        return 0.0
    return len(re.findall(r"[\u4e00-\u9fff]", text)) / len(text)

def page_urls(site):
    if "crawl" in site:
        out = []
        for seed in site["crawl"]:
            html = fetch(site["base"] + seed)
            for m in re.finditer(r'href="(/[a-zA-Z0-9_\-/#%]+)"', html):
                path = m.group(1).split("#")[0].rstrip("/")
                if not path:
                    continue
                if any(path.startswith(k) for k in site["keep"]):
                    out.append(site["base"] + path)
        seen = set()
        return [u for u in out if not (u in seen or seen.add(u))]
    sm = fetch(site["base"] + "/sitemap.xml")
    urls = re.findall(r"<loc>(.*?)</loc>", sm)
    out = []
    for u in urls:
        if not u.endswith(".html"):
            continue
        path = u[len(site["base"]):]
        if any(path.startswith(k) for k in site["keep"]):
            out.append(u)
    return out

def fname_of(site, url):
    path = url[len(site["base"]):]
    if path.endswith(".html"):
        path = path[:-5]
    path = path.strip("/")
    return f"{site['name']}_{path.replace('/', '_')}.md"

def process(site, url):
    if site["md"]:
        try:
            md = clean_vue_md(fetch(url.replace(".html", ".md")))
        except Exception:
            md = None  # .md 端点不可用 → 降级到 HTML 正文提取
    if not site["md"] or md is None:
        p = MDifier()
        p.feed(extract_main(fetch(url)))
        md = p.text()
    if len(md) < 200 or cjk_ratio(md) < 0.02:
        return None
    return md

def main(mode):
    if mode == "test":
        md = process(SITES[0], "https://cn.vuejs.org/guide/introduction.html")
        print("长度:", len(md))
        print(md[:500])
        return
    os.makedirs(OUT_DIR, exist_ok=True)
    total_pages = total_files = total_chars = 0
    for site in SITES:
        try:
            urls = page_urls(site)
        except Exception as e:
            print(f"[跳过] {site['name']}: 页面列表获取失败 {e}")
            continue
        print(f"[{site['name']}] {len(urls)} 页")
        for n, url in enumerate(urls, 1):
            fname = fname_of(site, url)
            if os.path.exists(os.path.join(OUT_DIR, fname)):
                continue  # 已存在，跳过
            try:
                md = process(site, url)
            except Exception as e:
                print(f"  失败 {url}: {e}")
                continue
            time.sleep(DELAY)
            if md:
                with open(os.path.join(OUT_DIR, fname), "w", encoding="utf-8") as f:
                    f.write(md)
                total_files += 1
                total_chars += len(md)
            total_pages += 1
            if n % 20 == 0:
                print(f"  进度 {n}/{len(urls)}，已存 {total_files} 个文件")
    print(f"完成: {total_pages} 页抓取, 本轮新增 {total_files} 个文件, "
          f"约 {total_chars} 字 ≈ {total_chars // 450} 个 chunk")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "go")
