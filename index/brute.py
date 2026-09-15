# index/brute.py
from index.base import BaseRetriever

class BruteVectorRetriever(BaseRetriever):
    def __init__(self, chunks, embed_svc):
        # chunks: ingestion 的 Chunk 列表
        # embed_svc: EmbeddingService 实例——【由调用方传入】，不自己 new
        # 你要做：入库时把所有块的向量一次性算好（批处理），存成矩阵
        # self.vectors[i] 对应 chunks[i]
         self.vectors = embed_svc.encode_chunks(chunks)
         self.embed_svc = embed_svc

    def score(self, query: str) -> list[float]:
        # 编码查询 → 与每个块向量算相似度 → 长度=N 的分数列表
        q = self.embed_svc.encode_query(query)
        res = self.vectors @ q
        return res

    def search(self, query: str, k: int) -> list[int]:
        # 分数降序取前 k 个下标（和 BM25.search 一模一样的行为）
        s = self.score(query)
        return sorted(range(len(s)),key=lambda i:s[i], reverse=True)[:k]
