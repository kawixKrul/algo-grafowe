from queue import Queue
from typing import Tuple
from math import inf

from test import runtests


class Node:
    def __init__(self, value):
        self.parent = self
        self.rank = 0
        self.value = value


def find_set(x: Node):
    while x.parent != x:
        x = x.parent

    return x.parent


def union(x: Node, y: Node):
    x = find_set(x)
    y = find_set(y)

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def kruskal_algorithm(E: list[tuple[int, int, int]], n, s=0, t=1):
    V = [Node(i) for i in range(n)]
    min_weight = inf
    E.sort(key=lambda tup: -tup[2])

    for (x, y, c) in E:
        if find_set(V[s]) == find_set(V[t]):
            break
        if find_set(V[x - 1]) != find_set(V[y - 1]):
            union(V[x - 1], V[y - 1])
            min_weight = min(min_weight, c)

    return min_weight


def create_graph(V: int, L: Tuple[int, int, int]):
    graph = [[] for _ in range(V)]

    for (x, y, c) in L:
        graph[x - 1].append([y - 1, c])
        graph[y - 1].append([x - 1, c])

    return graph



def get_min_from_path(G):
    parent = [None for _ in range(len(G))]
    visited = [False for _ in range(len(G))]
    parent_edge = [0 for _ in range(len(G))]
    Q = Queue()
    Q.put(0)
    visited[0] = True
    while not Q.empty():
        u = Q.get()
        for (v, l) in G[u]:
            if not visited[v]:
                Q.put(v)
                visited[v] = True
                parent[v] = u
                parent_edge[v] = l
    curr = parent[1]
    edges = [parent_edge[1]]
    while curr is not None:
        edges.append(parent_edge[curr])
        curr = parent[curr]
    return min(edges[:-1])


def wrapper(V: int, L: Tuple[int, int, int]):
    result_kruskal = kruskal_algorithm(L, V)
    return result_kruskal


runtests(wrapper)
