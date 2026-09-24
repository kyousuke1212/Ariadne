# index/hnsw.py
"""HNSW 图索引——第 8 步成品。构图与搜索算法来自 scratch_hnsw2.py 的手写实现。
分层小世界图：上层稀疏长程边负责"坐飞机"，第 0 层负责"打车"。"""
import math
import random
import numpy as np
from index.base import BaseRetriever


def _assign_level(mL, rng):
    """抽签定层高。mL = 1/ln(M)。"""
    # TODO: 从 scratch 搬 assign_level，random 换成 rng
    return int(-math.log(rng.random()) * mL)


def _greedy_walk(graph, cur, qv, dotq):
    """一层内的纯爬山。"""
    # TODO: 从 scratch 搬 greedy_walk（含空邻接护栏），dotq 变成参数
    # （注意：scratch 里 dotq 用全局 vecs——库函数不许用全局，改传参数）
    while True:
        if not graph[cur]:
            return cur
            #   1. 看 cur 的所有邻居（graph[cur]），用 min 挑出离 q 最近的邻居 best
            #      （语法提示：min(graph[cur], key=lambda n: dist2(n, q))）
        best = max(graph[cur], key=lambda n: dotq(n, qv))
            #   2. 如果 best 比 cur 更近 → cur = best，继续循环
        if dotq(best,qv) > dotq(cur,qv) :
                    cur = best
            #   3. 否则 → 返回 cur（停下来了）
        else: 
            return cur


def _search_layer(graph, ep, qv, k, ef, vecs):
    candidates = {ep}
    visited = {ep}
    expanded = set()
    for _ in range(ef):
        pool = candidates - expanded
        if not pool:
            break
        # TODO ① 一枪一池：
        ids = list(pool)
        dots = vecs[ids] @ qv           # 一次矩阵乘 = 全池分数
        v = ids[int(np.argmax(dots))]   # argmax 顶替原来的 max(key=dotq)
        expanded.add(v)
        for nb in graph[v]:
            candidates.add(nb)
            visited.add(nb)
    # TODO ② 结尾一枪：
    ids = list(visited)
    dots = vecs[ids] @ qv               # 一趟拉完全部 visited 的分数
    top = np.argsort(-dots)[:k]         # 降序前 k 个位置
    return [ids[i] for i in top]        # 返回 list[int]，类型和原来一致



class HNSWIndex(BaseRetriever):
    def __init__(self, chunks, embed_svc, M=8, ef_c=40, ef=40, seed=42):
        # 和 brute 一样：入库时一次性编码全部块
        self.seed = seed
        self.chunks = chunks
        self.embed_svc = embed_svc
        self.vecs = embed_svc.encode_chunks(chunks)
        self.M, self.ef_c, self.ef = M, ef_c, ef
        self._build()

    # TODO: 把 scratch 的 build_hnsw 搬成私有方法 _build：
    #   1. rng = random.Random(seed)；order = list(range(N)); rng.shuffle(order)
    #   2. 逐个插入：抽签层高 → 加盖楼层 → 自顶向下降落 → 逐层连 M 个最近邻
    #      （新王登基时记得新高层 levels[l][i] = set()）
    #   3. 存成 self.levels / self.node_levels / self.entry
    def _build(self):
        rng = random.Random(self.seed)        # ① 专属骰子
        mL = 1 / math.log(self.M)             # ② 层高衰减系数，由 M 推出
        N = len(self.vecs)
        order = list(range(N))
        rng.shuffle(order)                    # ③ 乱序插入（8a 的实验结论）

        i0 = order[0]
        L0 = _assign_level(mL, rng)
        levels = [{} for _ in range(L0 + 1)]
        for l in range(L0 + 1):
            levels[l][i0] = set()
        node_levels = [0] * N
        node_levels[i0] = L0
        entry = i0

        for i in order[1:]:
            L = _assign_level(mL, rng)
            while len(levels) <= L:
                levels.append({})

            ep = entry
            for l in range(node_levels[entry], L, -1):
                ep = _greedy_walk(levels[l], ep, self.vecs[i], self._dotq)

            for l in range(min(L, node_levels[entry]), -1, -1):
                res = _search_layer(levels[l], ep, self.vecs[i],
                                    k=self.M, ef=self.ef_c, vecs=self.vecs)
                levels[l].setdefault(i, set()).update(res)
                for nb in res:
                    levels[l][nb].add(i)
                ep = res[0]

            node_levels[i] = L
            if L > node_levels[entry]:
                for l in range(node_levels[entry] + 1, L + 1):
                    levels[l][i] = set()      # 新王占坑（上次抓的 bug 别丢）
                entry = i

        self.levels = levels                  # ④ 结果存进 self
        self.node_levels = node_levels
        self.entry = entry


    def _dotq(self, idx, qv):
        return float(self.vecs[idx] @ qv)

    def _search(self, qv, k):
        """多层搜索，返回全部 visited 按分数降序的前 k 个。k 给 10**9 就是全部。"""
        # TODO: 从 scratch 搬 search（自顶向下 + 第 0 层 search_layer），
        #       dotq 传 self._dotq
        ep = self.entry                                            # ① 接力棒：从全局入口开始
        for L in range(self.node_levels[self.entry], 0, -1):            # ② 从最高层一路往下到第 1 层
            ep = _greedy_walk(self.levels[L], ep, qv,self._dotq)               # ③ 在第 L 层爬山，落点更新接力棒
        return _search_layer(self.levels[0], ep, qv, k, self.ef,self.vecs)         # ④ 第 0 层：候选池细搜

    def score(self, query: str) -> list[float]:
        """长度=N 的分数向量。未访问的块 = 0（无证据）。"""
        # TODO: 跑一次 _search(qv, 10**9)，把 visited 的分数填进长 N 的 0 向量
        qv = self.embed_svc.encode_query(query)
        s = [0.0] * len(self.vecs)          # 没访问到的块 = 0（无证据）
        for i in self._search(qv, 10**9):   # k 巨大 → 返回全部 visited
            s[i] = self._dotq(i, qv)        # 访问过的块填真实分数
        return s

    def search(self, query: str, k: int) -> list[int]:
        # TODO: 一行：编码查询 → self._search(qv, k)
         return self._search(self.embed_svc.encode_query(query), k)