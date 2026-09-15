import json
import sys
sys.stdout.reconfigure(encoding="utf-8")
from ingestion.pipeline import build_chunks
from embed.service import EmbeddingService
from retrieve.bm25 import BM25
from index.brute import BruteVectorRetriever
from retrieve.fusion import RRFFusion, ScoreFusion

chunks = build_chunks("data")
bm25 = BM25(chunks)
brute = BruteVectorRetriever(chunks, EmbeddingService())
data = json.load(open("eval/dataset.json", encoding="utf-8"))

def recall_at_1(r):
    hit = total = 0
    for item in data:
        top1 = {chunks[i].chunk_id for i in r.search(item["question"], 1)}
        hit += len(top1 & set(item["relevant"]))
        total += len(item["relevant"])
    return hit / total

print("=== 权重扫描：两种融合策略对比 ===")
print("w向量/wBM25 | RRF融合 | 分数融合")
for w in [1.0, 1.1, 1.25, 1.5, 2.0, 3.0]:
    rrf = RRFFusion([bm25, brute], weights=[1.0, w])
    sf = ScoreFusion([bm25, brute], weights=[1.0, w])
    print(f"   {w:<5}   |  {recall_at_1(rrf):.3f}  |  {recall_at_1(sf):.3f}")
