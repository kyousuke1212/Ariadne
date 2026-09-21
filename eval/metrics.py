def recall_at_k(ranked_ids: list[str],relevant: set[str],k: int)-> float:
    top_k = set(ranked_ids[:k])
    hit = top_k & relevant
    return len(hit) / len(relevant)

def mrr(ranked_ids: list[str], relevant: set[str], k:int) -> float:
    for i, cid in enumerate(ranked_ids[:k]):
        if cid in relevant:
            return 1 / (i + 1)
    return 0.0

if __name__ == "__main__":
    rel = {"c1", "c4"}
    assert recall_at_k(["c2", "c1", "c0"], rel, 3) == 0.5
    assert mrr(["c2", "c1", "c0"], rel, 3) == 0.5

    # 练1：relevant = {a}，检索前 3 位 = [b, a, c]
    assert recall_at_k(["b", "a", "c"], {"a"}, 1) == 0.0    # 第 1 位是 b，没命中
    assert recall_at_k(["b", "a", "c"], {"a"}, 3) == 1.0    # a 在第 3 位，1/1
    assert mrr(["b", "a", "c"], {"a"}, 3) == 1/2            # a 排第 3 → 1/3
    # 练2：relevant = {x, y}，前 3 位 = [y, z, w]
    assert recall_at_k(["y", "z", "w"], {"x", "y"}, 3) == 0.5
    assert mrr(["y", "z", "w"], {"x", "y"}, 3) == 1.0
    # 练3：relevant = {p}，前 5 位 = [q, r, s, t, u]
    assert mrr(["q", "r", "s", "t", "u"], {"p"}, 5) == 0.0

    print("对拍通过")
