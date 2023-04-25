# bfs
# adding the number of neighbors
class Node:
    def __init__(self, x):
        self.x = 0

class Graph:
    def __init__(self, v, e):
        self.v = v
        self.e = e
        self.adjmatrix = [[0 for i in range(v)] for j in range(v)]

    def addEdge(self, u, v):
        if u == v:
            return
        self.adjmatrix[u][v] = 1
        self.adjmatrix[v][u] = 1
    
    def countSquawks(self, s, t):
        explored = [False] * self.v
        q = [s]
        explored[s] = True
        weights = [0 for i in range(self.v)]

        for i in range(t):
            print(f"t={i}")
            counter = 0
            current = q[0]
            q = q[1:]

            for i in range(self.v):
                if (self.adjmatrix[current][i]):

                    weights[i] += 1
                    # for j in range(self.v):
                    #     if (self.adjmatrix[i][j]):
                    #         weights

                    print(f"giving {self.adjmatrix[current][i] + weights[current]} squawks from vertex {current} to vertex {i}")
                    counter += self.adjmatrix[current][i] + weights[current]
                    print(f"no of squawks is: {counter}")
                    q.append(i)
                    explored[i] = True
            weights[current] = 0
            print("###")
        
        return counter

n, m, s, t = list(map(lambda x: int(x), input().split(" ")))

g = Graph(n, m)

for i in range(m):
    x, y = list(map(lambda x: int(x), input().split(" ")))
    g.addEdge(x, y)

print(g.countSquawks(s, t))