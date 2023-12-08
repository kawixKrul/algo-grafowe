from queue import PriorityQueue


class Node:
    def __init__(self):
        self.edges = {}
        self.active = True

    def add_edge(self, node, weight):
        self.edges[node] = self.edges.get(node, 0) + weight

    def remove_edge(self, node):
        del self.edges[node]


def merge_vertexes(G, u, v):
    y_list = list(G[v].edges.items())
    for vertex, weight in y_list:
        if vertex != u:
            G[u].add_edge(vertex, weight)
            G[vertex].add_edge(u, weight)
        G[v].remove_edge(vertex)
        G[vertex].remove_edge(v)


def minimum_cut_phase(G):
    n = len(G)
    a = 0
    S = []
    queue=PriorityQueue()
    queue.put((0, a))
    visited = [False for _ in range(n)]
    weights = [0 for _ in range(n)]
    while not queue.empty():
        v_weight, v = queue.get()
        if not visited[v]:
            S.append(v)
            visited[v] = True
            for u, u_weight in G[v].edges.items():
                if not visited[u]:
                    weights[u] += u_weight
                    queue.put((-weights[u], u))
    s = S[-1]
    t = S[-2]
    res = 0
    for v, weight in G[s].edges.items():
        res += weight
    merge_vertexes(G, t, s)
    return res


def stoer_wagner(V, L):
    G = [Node() for _ in range(V)]
    for (x, y, c) in L:
        G[x - 1].add_edge(y - 1, c)
        G[y - 1].add_edge(x - 1, c)
    res = float('inf')
    while V > 1:
        res = min(res, minimum_cut_phase(G))
        V -= 1
    return res