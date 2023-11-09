def update_weights(Graph: list[tuple[int, int]], path: list[int], minW: int):
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        for idx, (vertex, flow) in enumerate(Graph[u]):
            if vertex == v:
                Graph[u][idx] = (vertex, flow - minW)
                break

        for idx, (vertex, flow) in enumerate(Graph[v]):
            if vertex == u:
                Graph[v][idx] = (vertex, flow + minW)
                break


def augmenting_path(Graph: list[tuple[int, int]], source: int, sink: int, graph_search_func):
    n = len(Graph)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    # flow between vertex v and u = parent[v]
    flowBetween = [0 for _ in range(n)]

    graph_search_func(Graph, source, visited, parent, flowBetween)

    path = []
    minW = 0

    if visited[sink]:
        v = sink
        minW = flowBetween[v]  # same result as float('inf')
        while v != source:
            path.append(v)
            minW = min(minW, flowBetween[v])
            v = parent[v]
        path.append(source)
        path.reverse()

    return path, minW


def FordFulkerson_List(List: list[tuple[int, int]], s: int, t: int, graph_search_func):
    count = 0
    augPath, minW = augmenting_path(List, s, t, graph_search_func)
    while augPath:
        update_weights(List, augPath, minW)
        count += minW
        augPath, minW = augmenting_path(List, s, t, graph_search_func)

    return count




