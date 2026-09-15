from ingestion.pipeline import build_chunks
from embed.service import EmbeddingService
from index.brute import BruteVectorRetriever

chunks = build_chunks("data")
brute = BruteVectorRetriever(chunks, EmbeddingService())

# ① 契约检查：score 长度必须 = 块数 4
scores = brute.score("谁负责用户画像系统？")
assert len(scores) == 4, f"score 长度错误: {len(scores)}"

# ② 语义题：BM25 的死穴题，向量必须拿下
top = brute.search("谁让公司的业务从亏钱变成赚钱？", 1)
assert chunks[top[0]].chunk_id == "团队介绍.md-1", f"语义题失败: {top}"

# ③ 精确题：向量也不能输给 BM25
top = brute.search("谁管理了500多个节点的Kubernetes集群？", 1)
assert chunks[top[0]].chunk_id == "团队介绍.md-0", f"精确题失败: {top}"

print("✅ 暴力向量检索器对拍通过")
