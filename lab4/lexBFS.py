class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()
        self.RN= set()
        self.parent = None

    def connect_to(self, v):
        self.out.add(v)


def make_graph(V, L):
    G = [None] + [Node(i) for i in range(1, V+1)]  # żeby móc indeksować numerem wierzchołka

    for (u, v, _) in L:
        G[u].connect_to(v)
        G[v].connect_to(u)
    return G


def lexBFS(Graph):
    visited = []
    vertices = [set(range(1, len(Graph)))]
    while len(visited) < len(Graph) - 1:
        u = vertices[-1].pop()
        visited.append(u)
        idx = 0
        while idx < len(vertices):
            i = 0
            neighbours = vertices[idx] & Graph[u].out
            not_neighbours = vertices[idx] - neighbours
            if len(neighbours) > 0:
                vertices.insert(idx+1, neighbours)
                i += 1
            if len(not_neighbours) > 0:
                vertices.insert(idx+1, not_neighbours)
                i += 1
            vertices.remove(vertices[idx])
            idx += 1
        new_vertices = []
        intersection = set()
        for v in visited:
            new_vertices.append(v)
            intersection.add(v)
        Graph[u].RN = intersection & Graph[u].out
        found = False
        while len(new_vertices) > 0 and not found:
            if {new_vertices[-1]} & Graph[u].RN == set():
                new_vertices.pop(-1)
            else:
                found = True
        if found:
            Graph[u].parent = new_vertices[-1]
    return visited


def coloring(V, L):
    G = make_graph(V, L)
    visited = lexBFS(G)
    colors = [0] * len(G)
    for v in visited:
        used = {colors[u] for u in G[v].out}
        j = 1
        while j in used:
            j += 1
        colors[v] = j
    return max(colors)


def max_clique(V, L):
    G = make_graph(V, L)
    visited = lexBFS(G)
    res = 0
    for v in visited:
        res = max(res, len(G[v].RN) + 1)
    return res


def chordal(V, L):
    Graph = make_graph(V, L)
    visited = lexBFS(Graph)
    for v in visited[1:]:
        if not Graph[v].RN - {Graph[v].parent} <= Graph[Graph[v].parent].RN:
            return False
    return True


def vertex_cover(V ,L):
    G = make_graph(V, L)
    visited = lexBFS(G)
    I = set()
    for v in visited:
        N = I & G[v].out
        if I & N == set():
            I.add(v)
    return len({v for v in range(1, len(G))} - I)