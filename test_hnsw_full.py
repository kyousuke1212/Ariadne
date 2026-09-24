# test_hnsw_full.py —— 8c-2 全量考场：3520 块 × 93 题，追判官 ≥ 0.9
# 慢：判官和考生各编码一遍 3520 块 + 构图 3520 节点，预计 3~8 分钟，中途别关
# 本卷：同一张图连考 ef=40/80/160——ef 是搜索预算，idx.ef 随时可改，构图只需一次
import sys, json, time
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
from ingestion.pipeline import build_chunks
from embed.service import EmbeddingService
from index.brute import BruteVectorRetriever
from index.hnsw import HNSWIndex

DATA_DIR = str(Path(__file__).resolve().parent / "data")
chunks = build_chunks(DATA_DIR)
print(f"全量语料: {len(chunks)} 块")

DS_PATH = Path(__file__).resolve().parent / "eval" / "dataset.json"
dataset = json.loads(DS_PATH.read_text(encoding="utf-8"))
questions = [item["question"] for item in dataset]

svc = EmbeddingService()
brute = BruteVectorRetriever(chunks, svc)   # 判官：编码 3520 块
idx = HNSWIndex(chunks, svc)                # 考生：再编一遍 + 构图（最慢的一步）
print(f"构图完成: {len(idx.levels)} 层, 每层节点数 {[len(lv) for lv in idx.levels]}")

def exam(ef):
    """全部 93 题跑一遍。ef 是搜索预算——考生属性，构图完随便改。"""
    idx.ef = ef
    t0 = time.perf_counter()
    ovs = []
    for q in questions:
        judge = set(brute.search(q, 10))
        mine = set(idx.search(q, 10))
        ovs.append(len(judge & mine) / 10)
    dt = time.perf_counter() - t0
    avg = sum(ovs) / len(ovs)
    print(f"ef={ef}: 重叠率 {avg:.3f}（93 题共 {dt:.1f}s，均 {dt/len(questions)*1000:.0f} ms/题）")
    return ovs

ovs40  = exam(40)
ovs80  = exam(80)
ovs160 = exam(160)

# 卡得最狠的 3 题——裂缝在低分题里显形；并排看 ef 加大后它被救回来没有
for i in sorted(range(len(ovs40)), key=lambda i: ovs40[i])[:3]:
    print(f"\n卡住的题: {questions[i]}")
    print(f"  ef=40/80/160 重叠率: {ovs40[i]}/{ovs80[i]}/{ovs160[i]}")
    print(f"  判官第一名: [{chunks[brute.search(questions[i], 10)[0]].text[:40]}]")
    print(f"  我的第一名: [{chunks[idx.search(questions[i], 10)[0]].text[:40]}]")
