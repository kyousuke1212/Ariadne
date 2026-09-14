from ingestion.pipeline import build_chunks
from retrieve.bm25 import BM25

chunks = build_chunks("data")
bm = BM25(chunks)

queries = [
    ("谁负责用户画像系统", "高松灯"),
    ("Kubernetes", "椎名立希"),
    ("智能客服", "要乐奈"),
    ("BM25 算法", "BM25"),
    ("HNSW 索引", "HNSW"),
    ("年营收", "长崎爽世"),
]
for q, expect in queries:
    top = bm.search(q, 3)
    print(q, "->", [(i, chunks[i].text[:15].replace("\n", "")) for i in top])
    ok = any(expect in chunks[i].text for i in top[:1])
    print("  第一名含", expect, ":", "✅" if ok else "❌")
