# https://open.kattis.com/problems/laptopsticker

wc, hc, ws, hs = list(map(lambda x: int(x), input().split(" ")))
if (wc-ws > 1) and (hc-hs > 1):
    print(1)
else:
    print(0)