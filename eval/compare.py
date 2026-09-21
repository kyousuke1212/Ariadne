# -*- coding: utf-8 -*-
"""对比台：多个检索器 × 同一数据集 → 总表 + 分题型表 + 逐题对比（⭐分歧题）。

打印在这里做；同时返回 reports dict，别的脚本可以程序化使用。
"""
import os, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from eval.evaluate import evaluate


def compare(retrievers, dataset, chunks, k=10):
    """retrievers: {名字: 检索器实例}。检索器实例由调用方创建——构造成本高的
    （比如要加载嵌入模型的）在多个名字间共享，这就是依赖注入的用法。"""
    reports = {name: evaluate(r, dataset, chunks, k) for name, r in retrievers.items()}
    names = list(retrievers)

    print("=== 正式考试：" + " vs ".join(names) + " ===")
    for label, field in [("Recall@1", "recall1"), ("Recall@3", "recall3")]:
        parts = []
        for n in names:
            h, t = reports[n]["summary"][field]
            parts.append(f"{n}={h}/{t}={h/t:.3f}")
        print(f"{label}: " + "  ".join(parts))
    print("MRR@10: " + "  ".join(f"{n}={reports[n]['summary']['mrr']:.3f}" for n in names))
    print("平均延迟: " + "  ".join(f"{n}={reports[n]['summary']['avg_ms']:.0f}ms" for n in names))

    cats = sorted({q["category"] for q in dataset})
    print("\n--- 分题型 Recall@1 ---")
    for cat in cats:
        parts = []
        for n in names:
            h, t = reports[n]["by_category"].get(cat, {"recall1": (0, 0)})["recall1"]
            parts.append(f"{n} {h}/{t}={h/t:.3f}" if t else f"{n} 无题")
        print(f"  {cat}: " + " | ".join(parts))

    print("\n=== 逐题对比 ===")
    per_q = reports[names[0]]["per_question"]  # 所有检索器跑的是同一套题，顺序一致
    for idx, q in enumerate(per_q):
        marks = [reports[n]["per_question"][idx]["hit1"] > 0 for n in names]
        row = " | ".join("✅" if m else "❌" for m in marks)
        star = " ⭐ 结果不同" if len(set(marks)) > 1 else ""
        print(f"{row}  {q['question']}  {star}")

    return reports
