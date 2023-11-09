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


def wrapper_kruskal(V: int, L: Tuple[int, int, int]):
    result_kruskal = kruskal_algorithm(L, V)
    return result_kruskal


runtests(wrapper_kruskal)
