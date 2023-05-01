# Problem: https://open.kattis.com/contests/thduyq/problems/increasingsubsequence

# Given constraint is 200
MAX = 201

while True:
    # Input
    sequence = list(map(lambda x: int(x), input().split(" ")))
    if sequence[0] == 0:
        break
    sequence = sequence[1:]
    memo = [-1] + [MAX] * len(sequence)

    # Find lengths for each sequence[i]
    lisLength = 0
    index = 0
    lengths = [None]*len(sequence)
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
        lengths[i] = low
        if lisLength < low:
            lisLength = low
            index = i
    
    # Find all largest increasing subsequences
    candidates = []
    longest = max(lengths)
    for i in range(len(lengths)):
        if lengths[i] == longest:
            candidates.append(i)

    # Reconstruct each sequence
    all_lis = []
    for index in candidates:
        lis = []
        j = 1
        while index > -1:
            if len(lis) == 0:
                lis.append(sequence[index])
            elif lis[0] > sequence[index] and lengths[index] == longest-j:
                lis = [sequence[index]] + lis
                j += 1
            index -= 1
        all_lis.append(lis)

    # Get lexicographically earliest and print answer
    ans = min(all_lis)
    print(len(ans), end=" ")
    for e in ans:
        print(e, end=" ")
    print("")