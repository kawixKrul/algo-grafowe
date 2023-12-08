from copy import deepcopy
from typing import Any
from lab2.flow_list import FordFulkerson_List
from lab2.searches import BFS_list


def convert_matrix(V, L) -> list[list[int]]:
    Matrix = [[0 for _ in range(V)] for _ in range(V)]
    for u, v, w in L:
        try:
            Matrix[u - 1][v - 1] = w

        except IndexError:
            print(f"IndexError: {u}, {v}, {w}")

    return Matrix


def convert_list(Matrix) -> list[list[Any]]:
    n = len(Matrix)
    Graph = [[] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if Matrix[u][v]:
                Graph[u].append((v, Matrix[u][v]))
                Graph[v].append((u, Matrix[v][u]))

    return Graph


def min_cut_flow(V, L):
    Graph = convert_list(convert_matrix(V, L))
    n = len(Graph)
    minCut = float('inf')

    for t in range(1, n):
        residual_graph = deepcopy(Graph)
        maxFlow = FordFulkerson_List(residual_graph, 0, t, BFS_list)
        minCut = min(minCut, maxFlow)

    return minCut