obstacles = set()
n, m = list(map(int, input().split(" ")))
for _ in range(m):
    obstacles.add(int(input()))
for i in range(n):
    if i not in obstacles:
        print(i)
print(f"Mario got {len(obstacles)} of the dangerous obstacles.")