from queue import Queue


def BFS_list(Graph, source, visited, parent, flowBetween):
    Q = Queue()

    Q.put(source)
    visited[source] = True

    while not Q.empty():
        u = Q.get()
        for idx, (v, f) in enumerate(Graph[u]):
            if f and not visited[v]:
                visited[v] = True
                parent[v] = u
                flowBetween[v] = f
                Q.put(v)


def DFS_list(Graph, source, visited, parent, flowBetween):
    Stack = [source]
    visited[source] = True

    while Stack:
        u = Stack.pop()
        for idx, (v, f) in enumerate(Graph[u]):
            if f and not visited[v]:
                visited[v] = True
                parent[v] = u
                flowBetween[v] = f
                Stack.append(v)


#################################################


def BFS_matrix(Graph, source, visited, parent):
    n = len(Graph)
    Q = Queue()

    Q.put(source)
    visited[source] = True

    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if Graph[u][v] and not visited[v]:
                parent[v] = u
                visited[v] = True
                Q.put(v)


def DFS_matrix(Graph, source, visited, parent):
    n = len(Graph)

    Stack = [source]
    visited[source] = True

    while Stack:
        u = Stack.pop()
        for v in range(n):
            if Graph[u][v] and not visited[v]:
                Stack.append(v)
                visited[v] = True
                parent[v] = u