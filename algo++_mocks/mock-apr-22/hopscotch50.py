def h(x1, x2, y1, y2):
    return abs(x1-x2) + abs(y1-y2)
def main():
    n, k = map(int, input().split())
    ans = float('inf')
    dp = [[] for i in range(k+1)]
    distances = [[float('inf')] * n for i in range(n)]
    for j in range(n):
        row = list(map(int, input().split()))
        for i in range(len(row)):
            dp[row[i]].append((i, j))
            if row[i] == 1:
                distances[i][j] = 0
                if k == 1:
                    ans = 0
    for i in range(k+1):
        if i < 2:
            continue
        for x1, y1 in dp[i]:
            for x2, y2 in dp[i-1]:
                curr_d = distances[x2][y2]
                if curr_d == float('inf'):
                    continue
                curr_d += h(x1, x2, y1, y2)
                if i == k:
                    ans = min(curr_d, ans)
                distances[x1][y1] = min(curr_d, distances[x1][y1])
    if ans < float('inf'):
        print(ans)
        return
    print(-1)
main()
