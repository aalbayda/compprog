#You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.

n = int(input())
given = list(map(lambda x: int(x), input().split(" ")))
given.sort()
total = 0
for num in given:
    total += num

print(int(n*(n+1)/2 - total))