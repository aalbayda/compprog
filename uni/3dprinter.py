# https://open.kattis.com/problems/3dprinter
# Exam item in CMSC128 (Intro to Software Engineering)

n = int(input())
days = 1
printers = 1

while printers < n:
    printers *= 2
    days += 1

print(days)