from index.base import BaseRetriever

class RRFFusion(BaseRetriever):
    def __init__(self, retrievers, weights = None) :
        #收一个列表
        self.retrievers = retrievers
        if weights is None:
            weights = [1.0] * len(retrievers)
        self.weights = weights

    def score(self,query) -> list [float] :
        #每个块一个融合分
        n = len(self.retrievers[0].score(query))
        fused = [0.0] * n

        for k,r in enumerate(self.retrievers):
            s = r.score(query)
            ranked = sorted(range(n), key = lambda i:s[i], reverse=True)
            for j, i in enumerate(ranked):
                fused[i] += 1 / (60 + j +1) * self.weights[k]
        return fused

    def search(self,query,k) -> list[int] :
        #降序取前k个下标
        s = self.score(query)
        return sorted(range(len(s)), key=lambda i: s[i], reverse=True)[:k]

class ScoreFusion(BaseRetriever):
    def __init__(self, retrievers, weights=None):
        #同 RRFFusion：收列表 + 可选权重，默认全 1
        self.retrievers = retrievers
        if weights is None:
            weights = [1.0] * len(retrievers)
        self.weights = weights

    def score(self, query) -> list[float]:
        n = len(self.retrievers[0].score(query))
        fused = [0.0] * n

        for k, r in enumerate(self.retrievers):
            s = r.score(query)
            # min-max 归一化：把这条腿的分数压到 [0,1]，变成"相对信心"
            lo, hi = min(s), max(s)
            if hi - lo < 1e-12:
                # 防除零：这条腿对所有块打同分（比如 BM25 全 0）→ 弃权
                continue
            for i in range(n):
                fused[i] += ((s[i] - lo) / (hi - lo)) * self.weights[k]
        return fused

    def search(self, query, k) -> list[int]:
        #降序取前k个下标
        s = self.score(query)
        return sorted(range(len(s)), key=lambda i: s[i], reverse=True)[:k]