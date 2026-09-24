# test_agent.py —— 第 9 步验证：Agent 真问答（3 题，含多跳题），引用块对拍 relevant
import sys, json
sys.stdout.reconfigure(encoding="utf-8")
from ingestion.pipeline import build_chunks
from embed.service import EmbeddingService
from retrieve.bm25 import BM25
from index.brute import BruteVectorRetriever
from retrieve.fusion import ScoreFusion
from agent.react import ReactAgent, SearchTool

chunks = build_chunks("data")
svc = EmbeddingService()
bm25 = BM25(chunks)
brute = BruteVectorRetriever(chunks, svc)
fusion = ScoreFusion([bm25, brute])          # 第 7 步冠军配置当 Agent 的检索工具
agent = ReactAgent(SearchTool(fusion, chunks, k=5), max_rounds=4)

dataset = json.load(open("eval/dataset.json", encoding="utf-8"))
questions = [
    "谁负责搭建产品矩阵体系？",
    "React 编译器要如何配置才能只对加了标记的函数进行编译，实现渐进式迁移？",
    "混合检索中，融合多路排序结果常用哪个算法？",
]

for q in questions:
    r = agent.ask(q)
    print("=" * 70)
    print("问题:", q)
    print("轮数:", r["rounds"], "| 引用:", r["sources"])
    print("答案:", r["answer"][:200])
    item = next((x for x in dataset if x["question"] == q), None)
    if item:
        hit = set(r["sources"]) & set(item["relevant"])
        print(f"对拍: 引用 {len(r['sources'])} 个块，命中相关块 {len(hit)}/{len(item['relevant'])}")
