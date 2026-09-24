# app/builder.py
"""共享构建：语料 + 检索器 + Agent 只建一次（依赖注入哲学的第 9 步应用）。
CLI / API / UI 三个入口都从这里拿成品，不重复编码。"""
from ingestion.pipeline import build_chunks
from embed.service import EmbeddingService
from retrieve.bm25 import BM25
from index.brute import BruteVectorRetriever
from retrieve.fusion import ScoreFusion
from agent.react import ReactAgent, SearchTool


def build_app():
    """返回 (chunks, agent)。构建耗时 1~3 分钟（编码 3520 块）。"""
    chunks = build_chunks("data")
    svc = EmbeddingService()
    fusion = ScoreFusion([BM25(chunks), BruteVectorRetriever(chunks, svc)])
    agent = ReactAgent(SearchTool(fusion, chunks, k=5), max_rounds=4)
    return chunks, agent


def print_answer(chunks, question: str, r: dict):
    """统一打印：答案 + 引用块的可读预览。"""
    print(f"问: {question}")
    print(f"答: {r['answer']}")
    if r["sources"]:
        by_id = {c.chunk_id: c for c in chunks}
        print("来源:")
        for sid in r["sources"]:
            c = by_id.get(sid)
            if c:
                print(f"  - [{sid}] ({c.source}) {c.text[:60]}...")
