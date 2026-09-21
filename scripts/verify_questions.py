# -*- coding: utf-8 -*-
"""
LLM 复核 gen_questions.py 生成的候选问题：
1. 问题是否合格（太泛/语料答不了 → 淘汰）
2. 备选池里哪些块也【包含能完整回答的信息】→ relevant 多选
输出: eval/verified.json   （复核明细，可审计）
      eval/dataset.json    （旧 13 条 + 复核通过的新题，评测集最终版）
用法: python scripts/verify_questions.py
"""
import json, os, re, sys, time
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from openai import OpenAI
from ingestion.pipeline import build_chunks

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"], base_url="https://api.deepseek.com")

PROMPT = """你是检索评测集的标注复核员。给定一个问题 Q 和若干候选文档块（每块有 id 和内容），请判断：
1. Q 是否合格：必须能仅凭这些块中的至少一个完整回答；太宽泛（答案需要语料外知识）或含糊不清 → 不合格
2. 对每个候选块判断：它是否【包含能完整回答 Q 所需的信息】→ relevant（可多选）
只输出一个 JSON 对象，不要任何其他文字：{{"keep": true/false, "relevant": ["块id", ...]}}
不合格的问题 relevant 为空数组。

Q: {question}

候选块：
{chunks}"""

def verify_one(cand, by_id):
    listed = [cand["from_chunk"]] + cand["pool"]
    blocks = "\n".join(f"[{cid}] {by_id[cid].text[:600]}" for cid in listed if cid in by_id)
    prompt = PROMPT.format(question=cand["question"], chunks=blocks)
    for attempt in range(2):
        try:
            resp = client.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.0,
                max_tokens=200,
            )
            raw = resp.choices[0].message.content
            m = re.search(r"\{.*\}", raw, re.S)
            out = json.loads(m.group(0)) if m else {}
            if isinstance(out.get("keep"), bool):
                rel = [x for x in out.get("relevant", []) if x in listed]
                if out["keep"] and not rel:
                    rel = [cand["from_chunk"]]  # 兜底：至少保住生成源块
                return out["keep"], rel
        except Exception as e:
            if attempt == 1:
                print(f"  复核失败: {e}")
                return True, [cand["from_chunk"]]  # 失败时保守保留，人工兜底
    return True, [cand["from_chunk"]]

def main():
    chunks = build_chunks("data")
    by_id = {c.chunk_id: c for c in chunks}
    cands = json.load(open("eval/candidates.json", encoding="utf-8"))
    print(f"开始复核 {len(cands)} 条候选...")

    verified = []
    for i, c in enumerate(cands, 1):
        keep, rel = verify_one(c, by_id)
        verified.append({**c, "keep": keep, "relevant": rel})
        print(f"  [{i}/{len(cands)}] {'保留' if keep else '淘汰'} {c['question'][:40]}"
              f" → relevant {len(rel)} 块")
        time.sleep(0.2)

    with open("eval/verified.json", "w", encoding="utf-8") as f:
        json.dump(verified, f, ensure_ascii=False, indent=2)

    kept = [v for v in verified if v["keep"]]
    print(f"复核完成: 保留 {len(kept)} / 淘汰 {len(verified) - len(kept)}")

    # 合并成最终评测集：旧 13 条原样保留 + 新题
    old = json.load(open("eval/dataset.json", encoding="utf-8"))
    new = [{"question": v["question"], "relevant": v["relevant"], "category": v["category"]}
           for v in kept]
    merged = old + new
    with open("eval/dataset.json", "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    print(f"评测集最终版: eval/dataset.json 共 {len(merged)} 条（旧 {len(old)} + 新 {len(new)}）")

if __name__ == "__main__":
    main()
