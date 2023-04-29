import sys
input = sys.stdin.readline
N, K = map(int, input().split())
res = float('inf')
P = [[] for _ in range(K+1)]
dist = [[float('inf')] * N for _ in range(N)]
for r in range(N):
    row = list(map(int, input().split()))
    for c, v in enumerate(row):
        P[v].append((r, c))
        if v == 1:
            dist[r][c] = 0
            if K == 1:
                res = 0
for i in range(len(P)):
    print(f"{i}: {P[i]}")
for k in range(2, K+1):
    for r1, c1 in P[k]:
        for r2, c2 in P[k-1]:
            d = dist[r2][c2]
            if d == float('inf'):
                continue
            d += abs(r1-r2) + abs(c1-c2)
            if k == K:
                res = min(d, res)
            dist[r1][c1] = min(dist[r1][c1], d)
print(-1 if res == float('inf') else res)
