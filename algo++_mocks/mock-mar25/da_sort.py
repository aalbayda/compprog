# Problem: https://open.kattis.com/contests/thduyq/problems/dasort

cases = int(input())
for _ in range(cases):
    # Input each case
    k, n = list(map(int, input().split()))
    a = list(map(int, input().split()))

    # Get length of LIS that starts with the smallest item
    # From the Increasing Subsequence problem https://open.kattis.com/contests/thduyq/problems/increasingsubsequence
    MAX = 1001 # Acts as infinity, since constraint is 1000
    sequence = a[a.index(min(a)):] # Must start with smallest item
    memo = [-1] + [MAX] * len(sequence)
    # DP+binary search solution to find lengths for each sequence[i]
    lisLength = 0
    index = 0
    for i in range(len(sequence)):
        low = 0
        high = lisLength
        while (low <= high):
            mid = (low+high)//2
            if (memo[mid] < sequence[i]):
                low = mid + 1
            else:
                high = mid - 1
        memo[low] = sequence[i]
        if lisLength < low:
            lisLength = low
            index = i
    print(a)
    print(lisLength)
    # Number of delete+append operations should be (length of arr - length of LIS starting with 1)
    print(k, n-lisLength)