def minWeight(Graph: list[list[int]], path: list[int]):
    minW = Graph[path[0]][path[1]]
    for i in range(1, len(path) - 1):
        minW = min(minW, Graph[path[i]][path[i + 1]])

    return minW


def updateWeights(Graph: list[list[int]], path: list[int], minW: int):
    for i in range(len(path) - 1):
        Graph[path[i]][path[i + 1]] -= minW
        Graph[path[i + 1]][path[i]] += minW


def augmentingPath(Graph: list[list[int]], source: int, sink: int, graph_search_func):
    n = len(Graph)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    graph_search_func(Graph, source, visited, parent)

    path = []
    if visited[sink]:
        v = sink
        while v != source:
            path.append(v)
            v = parent[v]
        path.append(source)
        path.reverse()

    return path


def FordFulkerson_Matrix(Matrix: list[list[int]], s: int, t: int, graph_search_func):
    count = 0
    augPath = augmentingPath(Matrix, s, t, graph_search_func)
    while augPath:
        minW = minWeight(Matrix, augPath)
        updateWeights(Matrix, augPath, minW)
        count += minW
        augPath = augmentingPath(Matrix, s, t, graph_search_func)

    return count