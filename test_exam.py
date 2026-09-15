import json
import sys
sys.stdout.reconfigure(encoding="utf-8")
from collections import defaultdict
from ingestion.pipeline import build_chunks
from embed.service import EmbeddingService
from retrieve.bm25 import BM25
from index.brute import BruteVectorRetriever
from retrieve.fusion import RRFFusion, ScoreFusion

chunks = build_chunks("data")
# 实例只创建一次，三个检索器共享。
# EmbeddingService() 构造时会加载整个模型——写三遍就加载三遍，时间和内存×3。
# 这就是第 4 期 Q9 依赖注入的收益：使用方只负责"用"，不负责"造"。
bm25 = BM25(chunks)
brute = BruteVectorRetriever(chunks, EmbeddingService())
retrievers = {
    "BM25": bm25,
    "暴力向量": brute,
    "RRF融合": RRFFusion([bm25, brute]),
    "分数融合": ScoreFusion([bm25, brute]),
}
data = json.load(open("eval/dataset.json", encoding="utf-8"))

print("=== 第三场正式考试：BM25 vs 暴力向量 vs RRF融合 ===\n")

results = {}
for name, r in retrievers.items():
    by_cat = defaultdict(lambda: [0, 0])
    hit1 = hit3 = total = 0
    per_q = {}
    for item in data:
        top1 = {chunks[i].chunk_id for i in r.search(item["question"], 1)}
        top3 = {chunks[i].chunk_id for i in r.search(item["question"], 3)}
        rel = set(item["relevant"])
        per_q[item["question"]] = (len(top1 & rel) > 0, len(top3 & rel) > 0)
        by_cat[item["category"]][0] += len(top1 & rel)
        by_cat[item["category"]][1] += len(rel)
        hit1 += len(top1 & rel); hit3 += len(top3 & rel); total += len(rel)
    results[name] = per_q
    print(f"{name}: Recall@1 = {hit1}/{total} = {hit1/total:.3f}   Recall@3 = {hit3}/{total}")
    for cat, (h, t) in by_cat.items():
        print(f"    {cat}: {h}/{t}")
    print()

print("=== 逐题对比（" + " | ".join(retrievers) + "）===")
for item in data:
    marks = [results[name][item["question"]][0] for name in retrievers]
    row = " | ".join("✅" if m else "❌" for m in marks)
    mark = "⭐ 结果不同" if len(set(marks)) > 1 else ""
    print(f"{row}  {item['question']}  {mark}")
