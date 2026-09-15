import sys
sys.stdout.reconfigure(encoding="utf-8")  # Windows GBK 控制台防崩
from ingestion.pipeline import build_chunks
from embed.service import EmbeddingService
from retrieve.bm25 import BM25
from index.brute import BruteVectorRetriever
from retrieve.fusion import ScoreFusion

chunks = build_chunks("data")
fusion = ScoreFusion([
    BM25(chunks),
    BruteVectorRetriever(chunks, EmbeddingService()),
])

# ① 契约检查：融合分长度必须 = 块数 4
scores = fusion.score("谁负责用户画像系统？")
assert len(scores) == 4, f"score 长度错误: {len(scores)}"

# ② 语义题：BM25 的死穴，向量腿的强信心要把它顶回来
top = fusion.search("谁让公司的业务从亏钱变成赚钱？", 1)
assert chunks[top[0]].chunk_id == "团队介绍.md-1", f"语义题失败: {top}"

# ③ 精确题：向量腿的死穴（英文 token Python），BM25 腿的强信心要把它顶回来
top = fusion.search("谁精通Python？", 1)
assert chunks[top[0]].chunk_id == "团队介绍.md-0", f"精确题失败: {top}"

print("分数融合对拍通过")
# 说明：本文件原考 RRFFusion，其断言②（语义题）被证明在香草 RRF 下必挂
#（镜像平局，详见第6期手册）。对拍对象已换为冠军 ScoreFusion。
