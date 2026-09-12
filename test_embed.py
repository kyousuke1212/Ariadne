from embed.service import EmbeddingService
from ingestion.pipeline import build_chunks

svc = EmbeddingService()
chunks = build_chunks("data")
vecs = svc.encode_chunks(chunks)
print("块数:", len(vecs))
print("每个向量维度:", len(vecs[0]))     # 预期 512
q = svc.encode_query("谁负责容器化平台？")
print("查询向量维度:", len(q))          # 预期 512
