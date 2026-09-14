import math
import jieba


class BM25:
    def __init__(self, chunks):
        # chunks: list[Chunk]（ingestion 的产出，分词结果已经在 .tokens 里！）
        # 你要完成"建索引"：统计 N、df、每篇文档长度、avgdl
        self.chunks = chunks
        self.n = len(chunks)
        self.df = {}
        self.doc_lens = []
        for c in chunks:
            for t in set(c.tokens):
                self.df[t] = self.df.get(t,0)+1
            self.doc_lens.append(len(c.tokens))
        self.avgdl = sum(self.doc_lens)/self.n

    def score(self, query: str) -> list[float]:
        # 输入：一句原始查询文本
        q_terms = {w for w in jieba.cut(query) if w.strip()}
        # 输出：与 chunks 等长的列表，第 i 个数 = 第 i 个 chunk 的 BM25 分数
        scores = []
        k1 = 1.5
        b = 0.75
        for c in self.chunks:
            total = 0.0
            
            for t in q_terms:
                df_t = self.df.get(t,0)
                idf = math.log((self.n-df_t+0.5) / (df_t+0.5) + 1)
                tf = c.tokens.count(t)*(k1+1)/(c.tokens.count(t)+k1*(1-b+b*len(c.tokens)/self.avgdl))
                total += idf*tf
            scores.append(total)
        return scores
        
    def search(self, query: str, k: int) -> list[int]:
        # 输入：查询 + 想取几个
        s = self.score(query)
        # 输出：分数最高的 k 个 chunk 的【下标】（在 chunks 里的位置，从高到低）
        return sorted(range(self.n),key=lambda i:s[i], reverse=True)[:k]
    
        # 注意：返回下标，不返回文本——融合阶段要靠下标对齐向量检索的结果
