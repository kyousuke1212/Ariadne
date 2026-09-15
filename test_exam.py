import json
import sys
sys.stdout.reconfigure(encoding="utf-8")
from collections import defaultdict
from ingestion.pipeline import build_chunks
from embed.service import EmbeddingService
from retrieve.bm25 import BM25
from index.brute import BruteVectorRetriever

chunks = build_chunks("data")
retrievers = {
    "BM25": BM25(chunks),
    "暴力向量": BruteVectorRetriever(chunks, EmbeddingService()),
}
data = json.load(open("eval/dataset.json", encoding="utf-8"))

print("=== 第二场正式考试：BM25 vs 暴力向量 ===\n")

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

print("=== 逐题对比（BM25 | 暴力向量）===")
for item in data:
    a = results["BM25"][item["question"]][0]
    b = results["暴力向量"][item["question"]][0]
    mark = "⭐ 结果不同" if a != b else ""
    print(f"{'✅' if a else '❌'} | {'✅' if b else '❌'}  {item['question']}  {mark}")
