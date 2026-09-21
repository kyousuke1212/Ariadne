# -*- coding: utf-8 -*-
"""评测器：一个检索器 × 一份数据集 → 一份结构化报告（dict）。

设计原则：
- 数据进、数据出：不打印、不碰文件——打印是 compare.py 的事
- 每道题只检索一次 k=10：Recall@1 / Recall@3 / MRR@10 都从这一次结果里切片
  （检索结果的前缀性质：top10 的前 3 个就是 top3）
- 索引 → chunk_id 的转换只在这一层做（metrics.py 不认识语料，只认 id 字符串）
- 延迟：每道题只计 search 的耗时，不含检索器构造（那是冷启动，不是查询延迟）
"""
import os, sys, time
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from eval.metrics import recall_at_k, mrr


def evaluate(retriever, dataset, chunks, k=10):
    """跑完整个数据集，返回报告 dict：
    {
      "per_question": [{question, category, rel_count, hit1, hit3, mrr, ms, top_ids}],
      "summary":      {"recall1": (命中块数, 相关块数), "recall3": (...), "mrr": float, "avg_ms": float},
      "by_category":  {类别: 同 summary 的字段},
    }
    """
    per_q = []
    agg = {"hit1": 0, "hit3": 0, "mrr": 0.0, "rel": 0, "ms": 0.0}
    by_cat = {}

    for item in dataset:
        t0 = time.perf_counter()
        top = retriever.search(item["question"], k)
        ms = (time.perf_counter() - t0) * 1000

        ranked_ids = [chunks[i].chunk_id for i in top]  # 索引 → chunk_id
        rel = set(item["relevant"])
        # 三个指标都来自 metrics.py：它是"评分的唯一真理源"
        r1 = recall_at_k(ranked_ids, rel, 1)
        r3 = recall_at_k(ranked_ids, rel, 3)
        m = mrr(ranked_ids, rel, k)
        hit1 = round(r1 * len(rel))  # 命中块数 = 命中率 × 相关块数
        hit3 = round(r3 * len(rel))  # round 抹掉浮点误差（1/3*3 可能是 0.9999…）

        per_q.append({
            "question": item["question"],
            "category": item["category"],
            "rel_count": len(rel),
            "hit1": hit1, "hit3": hit3, "mrr": m, "ms": ms,
            "top_ids": ranked_ids,  # 逐题明细：翻车题诊断就靠它
        })
        agg["hit1"] += hit1
        agg["hit3"] += hit3
        agg["mrr"] += m
        agg["rel"] += len(rel)
        agg["ms"] += ms
        c = by_cat.setdefault(item["category"],
                              {"hit1": 0, "hit3": 0, "mrr": 0.0, "rel": 0, "n": 0})
        c["hit1"] += hit1
        c["hit3"] += hit3
        c["mrr"] += m
        c["rel"] += len(rel)
        c["n"] += 1

    n = len(dataset)
    summary = {
        "recall1": (agg["hit1"], agg["rel"]),
        "recall3": (agg["hit3"], agg["rel"]),
        "mrr": agg["mrr"] / n,
        "avg_ms": agg["ms"] / n,
    }
    by_category = {cat: {
        "recall1": (c["hit1"], c["rel"]),
        "recall3": (c["hit3"], c["rel"]),
        "mrr": c["mrr"] / c["n"],
    } for cat, c in by_cat.items()}

    return {"per_question": per_q, "summary": summary, "by_category": by_category}
