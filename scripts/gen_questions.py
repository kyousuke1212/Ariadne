# -*- coding: utf-8 -*-
"""
用 DeepSeek 从新语料块生成评测问题候选 + 检索器备选池。
用法（在项目根目录跑）: python scripts/gen_questions.py [采样块数, 默认 40]
输出: eval/candidates.json          （机读: 问题/题型/来源块/备选池）
      eval/candidates_review.md     （人工确认用: 勾选 relevant）
"""
import json, os, random, re, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import OpenAI
from ingestion.pipeline import build_chunks
from embed.service import EmbeddingService
from retrieve.bm25 import BM25
from index.brute import BruteVectorRetriever

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"], base_url="https://api.deepseek.com")

PROMPT = """你是检索系统评测集设计助手。给定一个文档片段（已切块），请生成 {n} 条中文检索问题，要求：
1. 问题必须能仅凭该片段完整回答（答案在该片段内）
2. 措辞尽量改写，不要直接复制片段原文的长句（用于测试语义检索）
3. 题型四选一：概念术语（某个概念是什么/怎么理解）、数字精确（具体参数/数值/版本）、命名精确（组件名/API名/属性名/函数名）、语义改写（换说法问同一件事）
4. 不要生成泛泛的常识问题（比如"什么是前端框架"）
5. 只输出 JSON 数组，不要任何其他文字：[{{"question": "...", "category": "..."}}]

片段如下：
---片段开始---
{chunk}
---片段结束---"""

CATS = {"概念术语", "数字精确", "命名精确", "语义改写"}

def gen_for_chunk(chunk_text, n=2):
    prompt = PROMPT.format(n=n, chunk=chunk_text)
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=800,
    )
    raw = resp.choices[0].message.content
    m = re.search(r"\[.*\]", raw, re.S)
    if not m:
        raise ValueError(f"LLM 输出不是 JSON 数组: {raw[:200]}")
    items = json.loads(m.group(0))
    out = []
    for it in items:
        if it.get("question") and it.get("category") in CATS:
            out.append({"question": it["question"].strip(), "category": it["category"]})
    return out

def write_review(candidates, chunks):
    """生成人工确认文件：每条问题列出生成源块 + 备选池勾选框，附块内容摘录，
    这样勾选时不用翻原文文件。"""
    by_id = {c.chunk_id: c for c in chunks}
    lines = ["# 评测问题候选 · 人工确认表", "",
             "规则：每条问题，把【能完整回答它的所有块】勾上（可多选），其余不勾。",
             "默认已勾了生成源块（问题就是从它生成的，一般都对）；",
             "重点看备选池里有没有【同样能回答】的块，有就勾上；",
             "如果问题本身不合格（太泛/答案不在语料），把整条划掉或标注「删」。",
             ""]
    for i, c in enumerate(candidates, 1):
        lines.append(f"### {i}. [{c['category']}] {c['question']}")
        lines.append("")
        seen = set()
        for cid in [c["from_chunk"]] + c["pool"]:
            if cid in seen:
                continue
            seen.add(cid)
            mark = "x" if cid == c["from_chunk"] else " "
            excerpt = " ".join(by_id[cid].text.split())[:100] if cid in by_id else ""
            lines.append(f"- [{mark}] {cid}  —  {excerpt}")
        lines.append("")
    with open("eval/candidates_review.md", "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def main():
    n_sample = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    chunks = build_chunks("data")
    new = [c for c in chunks if c.source.startswith(("vue_", "react_"))]
    if not new:
        print("data/ 里没有新语料（vue_/react_ 前缀），先跑 fetch_docs.py go")
        return
    by_file = {}
    for c in new:
        by_file.setdefault(c.source, []).append(c)
    random.seed(42)
    files = random.sample(sorted(by_file), min(n_sample, len(by_file)))
    sampled = [by_file[f][len(by_file[f]) // 2] for f in files]

    print(f"新语料 {len(new)} 块 / {len(by_file)} 个文件，采样 {len(sampled)} 块")
    print("加载检索器（首次编码全部块，可能要几分钟）...")
    bm = BM25(chunks)
    brute = BruteVectorRetriever(chunks, EmbeddingService())

    candidates = []
    for i, c in enumerate(sampled, 1):
        try:
            qs = gen_for_chunk(c.text)
        except Exception as e:
            print(f"  块 {c.chunk_id} 生成失败: {e}")
            continue
        for q in qs:
            pool = set(bm.search(q["question"], 5))
            pool |= set(brute.search(q["question"], 5))
            candidates.append({
                "question": q["question"],
                "category": q["category"],
                "from_chunk": c.chunk_id,
                "pool": [chunks[j].chunk_id for j in sorted(pool)],
            })
        print(f"  [{i}/{len(sampled)}] {c.chunk_id} → {len(qs)} 条")

    os.makedirs("eval", exist_ok=True)
    with open("eval/candidates.json", "w", encoding="utf-8") as f:
        json.dump(candidates, f, ensure_ascii=False, indent=2)
    write_review(candidates, chunks)

    print(f"完成: {len(candidates)} 条候选 → eval/candidates.json")
    print("请打开 eval/candidates_review.md 人工确认（勾选 relevant 块）")

if __name__ == "__main__":
    main()
