# https://open.kattis.com/problems/moderatepace

from statistics import median
n = int(input())
d1 = list(map(lambda x: int(x), input().split(" ")))
d2 = list(map(lambda x: int(x), input().split(" ")))
d3 = list(map(lambda x: int(x), input().split(" ")))
for i in range(n):
    print(median([d1[i], d2[i], d3[i]]), end="")
    if i < n-1:
        print(" ", end="")
