def main():
    # vertices, edges
    n, m = list(map(int, input().split(" ")))
    g = [[] for _ in range(n)] #adjacency list
    edge_list = []
    for _ in range(m):
        edge = input().split(" ")
        s = int(edge[0])-1
        d = int(edge[1])-1
        g[s].append(d)
        g[d].append(s)
        edge_list.append({s+1,d+1})

    # cycle checking, all vertices must have even degree
    for v in g:
        if len(v)%2 != 0:
            print("impossible")
            return

    # Hierholzer's
    path = [0]
    circuit = []
    visited = {path[-1]}
    while path:
        vertex = path[-1]
        if g[vertex]:
            next = g[vertex].pop()
            if next not in visited:
                path.append(next)
                visited.add(next)
        else:
            circuit.append(path.pop())

    # reconstruct edges from circuit
    current_edge = set()
    print(circuit[::-1])
    for i in range(len(circuit)-1,-1,-1):
        current_edge.add(circuit[i]+1)
        if len(current_edge) == 2:
            print(edge_list.index(current_edge)+1)
            current_edge = {circuit[i]+1}

main()