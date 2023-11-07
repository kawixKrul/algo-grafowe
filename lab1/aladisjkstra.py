from math import inf
from queue import PriorityQueue
from typing import Tuple
from test import runtests, create_graph


def dijkstra_mod(Graph):
    s, t = 0, 1
    Q = PriorityQueue()
    n = len(Graph)
    distance = [0 for _ in range(n)]
    distance[s] = inf
    Q.put((-distance[s], s))
    while not Q.empty():
        u, v = Q.get()
        for (x, l) in Graph[v]:
            weight = min(l, distance[v])
            if weight > distance[x]:
                distance[x] = weight
                Q.put((-distance[x], x))
    return distance[t]


def wrapper_dijkstra(V: int, L: Tuple[int, int, int]):
    result = dijkstra_mod(create_graph(V,L))
    return result


runtests(wrapper_dijkstra)
