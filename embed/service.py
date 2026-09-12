import os
os.environ["HF_HUB_OFFLINE"] = "1"
from sentence_transformers import SentenceTransformer



class EmbeddingService:
    def __init__(self):
        # 加载 BGE 模型，存到 self.model
        from sentence_transformers import SentenceTransformer
        self.model = SentenceTransformer("BAAI/bge-small-zh-v1.5")

    def encode_chunks(self, chunks) -> list:
        # 输入：ingestion 产出的 Chunk 列表
        texts = [c.text for c in chunks]
        # 输出：与输入等长的向量列表，每个向量 512 维
        return self.model.encode(texts,normalize_embeddings=True)


    def encode_query(self, text: str) -> list:
        # 输入：一句查询文本
        query = "为这个句子生成表示以用于检索相关文章：" + text
        # 输出：一个 512 维向量
        vec = self.model.encode([query], normalize_embeddings=True)
        return vec[0]

