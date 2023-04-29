# https://open.kattis.com/problems/mazeman

# Construct graph
rows, cols = list(map(int, input().split(" ")))
g = [None] * rows
doors = []

# Initialize from input
for i in range(rows):
    g[i] = list(input())
    doors += list(map(lambda x: (i, x),[j for j, x in enumerate(g[i]) if x.isalpha() and x != "X"]))
visited = [[False for _ in range(cols)] for _ in range(rows)]
paths = dict()
for door in doors:
    paths[g[door[0]][door[1]]] = 0

# Check if wall / out of bounds / visited before
def isValid(row, col, visited):
    if (row < 0 or col < 0 or row >= rows or col >= cols):
        return False
    if (g[row][col].isalpha()):
        return False
    if visited[row][col]:
        return False
    return True

# DFS
def dfs(door_row, door_col, door, visited, paths):
    stack = [(door_row, door_col)]
    dRow = [0, 1, 0, -1]
    dCol = [-1, 0, 1, 0]
    while stack:
        cur = stack[-1]
        stack = stack[:-1]
        row, col = cur[0], cur[1]
        if (door_row == row and door_col == col) or isValid(row, col, visited):
            if g[row][col] == ".":
                paths[door] += 1
            visited[row][col] = True
            for i in range(4):
                next_row, next_col = row+dRow[i], col+dCol[i]
                stack.append((next_row, next_col))

def count_unvisited():
    unvisited = 0
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == "." and visited[i][j] == False:
                unvisited += 1
    return unvisited

def main():
    for door in doors:
        dfs(door[0], door[1], g[door[0]][door[1]], visited, paths)

    min_doors = 0
    for path in paths:
        if paths[path] > 0:
            min_doors +=1

    print(f"{min_doors} {count_unvisited()}")

main()