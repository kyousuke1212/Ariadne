# index/base.py
class BaseRetriever:
    def score(self, query: str) -> list[float]:
        raise NotImplementedError("子类必须实现 score")

    def search(self, query: str, k: int) -> list[int]:
        raise NotImplementedError("子类必须实现 search")
