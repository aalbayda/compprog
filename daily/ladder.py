# https://open.kattis.com/problems/ladder

from math import radians, sin, ceil
h, v = list(map(lambda x: int(x), input().split(" ")))
print(ceil(h/sin(radians(v)))) # derived from "soh" in sohcahtoa