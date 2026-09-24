# test_hnsw.py —— 8c-1 冒烟测：HNSWIndex 搬家零损耗验收
# 三条：① 自查询自己排第 1  ② 93 题追判官 ≥ 0.9（8b 原成绩 0.962）  ③ score() 契约
import sys, random, json
sys.stdout.reconfigure(encoding="utf-8")
from pathlib import Path
from ingestion.pipeline import build_chunks
from embed.service import EmbeddingService
from index.brute import BruteVectorRetriever
from index.hnsw import HNSWIndex

# ===== 考试语料（和 8b 一模一样：93 题相关块 + 随机填充到 500） =====
DATA_DIR = str(Path(__file__).resolve().parent / "data")
all_chunks = build_chunks(DATA_DIR)

DS_PATH = Path(__file__).resolve().parent / "eval" / "dataset.json"
dataset = json.loads(DS_PATH.read_text(encoding="utf-8"))
relevant_ids = set()
for item in dataset:
    relevant_ids |= set(item["relevant"])
by_id = {c.chunk_id: c for c in all_chunks}
rel_chunks = [by_id[cid] for cid in sorted(relevant_ids) if cid in by_id]

random.seed(42)
rest = [c for c in all_chunks if c.chunk_id not in relevant_ids]
fill = random.sample(rest, max(0, 500 - len(rel_chunks)))
chunks = rel_chunks[:500] + fill
print(f"考试语料: {len(chunks)} 块")

# ===== 建索引（构图在 __init__ 里一次性完成） =====
svc = EmbeddingService()
idx = HNSWIndex(chunks, svc)
brute = BruteVectorRetriever(chunks, svc)
print(f"构图完成: {len(idx.levels)} 层, 入口 {idx.entry}, "
      f"每层节点数 {[len(lv) for lv in idx.levels]}")

# ===== ① 自查询：随机 10 块当查询，第一名必须是自己 =====
random.seed(42)
qs = random.sample(range(len(chunks)), 10)
hit = 0
for i in qs:
    top = idx.search(chunks[i].text, 10)
    if top[0] == i:
        hit += 1
    else:
        print(f"  块 {i} 自查询第一名是 {top[0]}: [{chunks[top[0]].text[:30]}]")
print(f"① 自查询命中: {hit}/10")

# ===== ② 93 题追判官：搬家后不能掉成绩 =====
questions = [item["question"] for item in dataset]
ovs = []
for q in questions:
    judge = set(brute.search(q, 10))
    mine = set(idx.search(q, 10))
    ovs.append(len(judge & mine) / 10)
avg = sum(ovs) / len(ovs)
print(f"② 追判官重叠率: {avg:.3f}（8b 原成绩 0.962，验收线 0.9）")

# ===== ③ score() 契约三查 =====
q = questions[0]
s = idx.score(q)
nz = sum(1 for x in s if x != 0.0)
print(f"③ score 长度: {len(s)}（应 = {len(chunks)}）")
print(f"   非零分数块: {nz}（应 << 500——HNSW 只拜访一小撮）")
print(f"   score 第一名 == search 第一名: {max(range(len(s)), key=lambda i: s[i]) == idx.search(q, 1)[0]}")
