def diagonal(n):
    return n**2 - (n-1)

def main():
    n = int(input())
    for i in range(n):
        r, c = list(map(lambda x: int(x), input().split(" ")))
        if c == r:
            n = c
            print(diagonal(n))
            continue
        m = max(r,c)
        if m%2 == 0:
            if r > c:
                print(diagonal(m) + (r-c))
                continue
            if c > r:
                print(diagonal(m) - (c-r))
                continue
        else:
            if r > c:
                print(diagonal(m) - (r-c))
                continue
            if c > r:
                print(diagonal(m) + (c-r))
                continue
    
main()