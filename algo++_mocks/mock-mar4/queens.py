
n = int(input())
rows = []
cols = []

def validateRows():
    for i in range(len(rows)):
        for j in range(i+1, len(rows)):
            if rows[i] == rows[j]:
                return False
            if abs(rows[i]-rows[j]) == abs(i-j):
                return False
    return True

def validateCols():
    for i in range(len(cols)):
        for j in range(i+1, len(cols)):
            if cols[i] == cols[j]:
                return False
            if abs(cols[i]-cols[j]) == abs(i-j):
                return False
    return True

for i in range(n):
    col, row = list(map(lambda x: int(x), input().split(" ")))
    cols.append(col)
    rows.append(row)
if validateCols() or validateRows():
    print("CORRECT")
else:
    print("INCORRECT")
            