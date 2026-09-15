import json
import sys
sys.stdout.reconfigure(encoding="utf-8")
from collections import defaultdict
from ingestion.pipeline import build_chunks
from retrieve.bm25 import BM25

chunks = build_chunks("data")
bm = BM25(chunks)
data = json.load(open("eval/dataset.json", encoding="utf-8"))

def recall_at_k(k):
    hit, total = 0, 0
    for item in data:
        top = {chunks[i].chunk_id for i in bm.search(item["question"], k)}
        rel = set(item["relevant"])
        hit += len(top & rel)
        total += len(rel)
    return hit / total

print("=== BM25 基线考试 ===")
print("题目数:", len(data))
print("Recall@1:", round(recall_at_k(1), 3))
print("Recall@3:", round(recall_at_k(3), 3))

by_cat = defaultdict(lambda: [0, 0])
for item in data:
    top = {chunks[i].chunk_id for i in bm.search(item["question"], 1)}
    rel = set(item["relevant"])
    h = len(top & rel)
    by_cat[item["category"]][0] += h
    by_cat[item["category"]][1] += len(rel)

print("\n=== 分题型 Recall@1 ===")
for cat, (h, t) in by_cat.items():
    print(f"{cat}: {h}/{t}")

print("\n=== 逐题 ===")
for item in data:
    top = bm.search(item["question"], 1)
    top1 = chunks[top[0]].chunk_id if top else "无结果"
    ok = top1 in item["relevant"]
    print(("✅" if ok else "❌"), item["question"], "→", top1, "| 标准答案:", item["relevant"])
