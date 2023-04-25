def find_s2(n, s1):
    s2 = []
    for i in range(1, n+1):
        if i not in s1:
            s2.append(i)
    return s2

def find_s1(upper, n):
    s1 = []
    sum = 0
    for i in range(1,n+1):
        sum += i
        s1.append(i)
        if sum == upper:
            return s1
        if sum > upper:
            sum = 0
            s1 = []
        for j in range(1, n+1):
            if j != i:
                sum += j
                s1.append(j)
                if sum == upper:
                    return s1
                if sum > upper:
                    i = 1
                    sum = 0
                    s1 = []
    return s1

def main():
    n = int(input())
    all_sum = n*(n+1)/2
    if all_sum % 2 != 0:
        print("NO")
        return

    s1 = find_s1(all_sum/2, n)
    s2 = find_s2(n, s1)

    print("YES")
    print(len(s1))
    for s in s1:
        print(s,end=" ")
    print("")
    print(len(s2))
    for s in s2:
        print(s,end=" ")
    print("")

main()