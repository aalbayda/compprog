# Problem: https://open.kattis.com/contests/thduyq/problems/carousel

while True:
    n, m = list(map(lambda x: int(x), input().split(" ")))
    if n == m and n == 0:
        break
    deals = {}
    for i in range(n):
        a, b = list(map(lambda x: int(x), input().split(" ")))
        if a <= m:
            deals[f"Buy {a} tickets for ${b}"] = b/a
    if not deals:
        print("No suitable tickets offered")
    else:
        best = min(deals.values())
        print(max([e[0] for e in deals.items() if e[1] == best]))