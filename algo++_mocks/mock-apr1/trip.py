from collections import defaultdict

class Graph:
    def __init__(self, edges=()):
        self._nodes = set() # Set of nodes.
        self._out = defaultdict(set) # Map from node to set of out-neighbours.
        self._in = defaultdict(set) # Map from node to set of in-neighbours.
        self.edges = edges

        for m, n in self.edges:
            self.add_edge(m, n)

    def __iter__(self):
        return iter(self._nodes)

    def get_size(self):
        return  len(self._nodes)

    def get_edge_size(self):
        return len(self.edges)

    def add_edge(self, m, n):
        self._nodes.add(m)
        self._nodes.add(n)
        self._out[m].add(n)
        self._in[n].add(m)

    def remove_edge(self, m, n):
        self._out[m].remove(n)
        self._in[n].remove(m)

    def out_neighbours(self, node):
        return self._out[node]

    def in_degree(self, node):
        return len(self._in[node])

    def out_degree(self, node):
        return len(self._out[node])

    def degree(self, node):
        return self.in_degree(node) + self.out_degree(node)

    def print_graph(self):
        for node in self._nodes:            
            print '%s -> %s' % (node, self._out[node])

def pick_any(iterable):
    return next(iter(iterable))

class NoEulerianPath(Exception):
    """Exception raised when there is no Eulerian path."""

def is_bridge(graph, node):
    if(len(graph.out_neighbours(node)) == 1):
        return True
    return False

"""Verifies if graph is made up by bridges only"""
def bridges_only(graph):
    for node in graph:
        if(graph.out_degree(node) > 1):
            return False
    return True

"""Removes the edge from the graph"""
def burn_edge(graph, u, v):
        graph.remove_edge(u, v)
        graph.remove_edge(v, u)
        return v

""" Visits and deletes all edges until """
def fleury(edges):
    graph = Graph(edges)

    # Mapping from surplus of out-edges over in-edges to list of nodes
    # with that surplus.
    surplus = defaultdict(list)
    odd_degree_nodes = []
    for node in graph:
        in_degree = graph.in_degree(node)
        out_degree = graph.out_degree(node)
        degree_surplus = out_degree - in_degree

        if abs(degree_surplus) > 1:
            raise NoEulerianPath("Node {} has in-degree {} and out-degree {}."
                                 .format(node, in_degree, out_degree))

        surplus[degree_surplus].append(node)        
        if(len(graph.out_neighbours(node)) % 2 == 1):
            odd_degree_nodes.append(node)   

    if(len(odd_degree_nodes) != 0 and len(odd_degree_nodes) != 2):
        raise NoEulerianPath("Number of odd degree nodes is different than 0 or 2.")
    
    # If there are 0 odd vertices, start anywhere. If there are 2 odd vertices, start at one of them.
    if(len(odd_degree_nodes) == 0):
        node = pick_any(graph)
    else:
        node = pick_any(odd_degree_nodes)
    
    path = [node]

    while(graph.out_degree(node)):
        
        # Continuously deletes edges between visited neighbours and appends the path that is being taken
        neighbour = None
        while(True):
            neighbour = pick_any(graph.out_neighbours(node))

            # Visits a bridge if, and only if, the graph is made up by bridges only
            if(is_bridge(graph, neighbour) and bridges_only(graph)):
                path.append(burn_edge(graph, node, neighbour))
                break
            path.append(burn_edge(graph, node, neighbour))
            node = neighbour            

        # Continuously burns up the "bridges" until the graph has no edges left saving the path that is being taken
        while(is_bridge(graph, neighbour) and bridges_only(graph)):            
            neighbour = pick_any(graph.out_neighbours(neighbour))
            path.append(burn_edge(graph, node, neighbour))
            if(len(path) == graph.get_edge_size()):
                break
        break

    return path