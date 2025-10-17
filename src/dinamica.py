from typing import List, Tuple

Finca = List[Tuple[int, int, int]]


def roPD(finca: Finca):
    n = len(finca)
    if n == 0:
        return [], 0

    ts = [x[0] for x in finca]
    tr = [x[1] for x in finca]
    p = [x[2] for x in finca]

    N = 2 ** n
    total_tr = [0] * N
    for mask in range(1, N):
        j = (mask & -mask).bit_length() - 1
        total_tr[mask] = total_tr[mask ^ (1 << j)] + tr[j]

    INF = float('inf')
    dp = [INF] * N
    prev = [-1] * N
    dp[0] = 0

    for mask in range(1, N):
        for j in range(n):
            if mask & (1 << j):
                mask_wo_j = mask ^ (1 << j)
                finish_j = total_tr[mask]
                tard_j = max(0, finish_j - ts[j])
                cost = dp[mask_wo_j] + p[j] * tard_j
                if cost < dp[mask]:
                    dp[mask] = cost
                    prev[mask] = j

    perm = []
    mask = N - 1
    while mask:
        j = prev[mask]
        perm.append(j)
        mask ^= (1 << j)
    perm.reverse()
    return perm, dp[N - 1]


if __name__ == "__main__":
    finca = [(5, 3, 4), (4, 1, 3), (8, 2, 2), (3, 2, 4), (10, 3, 3)]
    perm, costo = roPD(finca)
    print("Permutación óptima:", perm)
    print("Costo mínimo:", costo)