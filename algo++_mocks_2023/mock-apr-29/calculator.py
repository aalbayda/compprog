# https://open.kattis.com/problems/calculator

while True:
    try:
        expr = input()
        ans = eval(expr)
        print("{:.2f}".format(ans))
    except:
        break