# -*- coding: utf-8 -*-
"""考试入口（第 7 步后瘦身版）：逻辑全部委托给 eval 模块。
用法: python test_exam.py
"""
import json, sys
sys.stdout.reconfigure(encoding="utf-8")
from ingestion.pipeline import build_chunks
from embed.service import EmbeddingService
from retrieve.bm25 import BM25
from index.brute import BruteVectorRetriever
from retrieve.fusion import RRFFusion, ScoreFusion
from eval.compare import compare

chunks = build_chunks("data")
# 检索器实例只创建一次、在多个融合器间共享（依赖注入）：
# EmbeddingService() 构造要编码全部 3500 块，写四遍就 ×4 的时间和内存。
bm25 = BM25(chunks)
brute = BruteVectorRetriever(chunks, EmbeddingService())
compare(
    {"BM25": bm25, "暴力向量": brute,
     "RRF融合": RRFFusion([bm25, brute]), "分数融合": ScoreFusion([bm25, brute])},
    json.load(open("eval/dataset.json", encoding="utf-8")),
    chunks,
)
