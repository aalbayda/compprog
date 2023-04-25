n = int(input())
l = list(map(lambda x: int(x), input().split(" ")))
moves = 0
prev = 0
for num in l:
    if num < prev:
        moves += (prev - num)
        num = prev
    prev = num
print(moves)