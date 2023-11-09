from test import runtests, create_graph


def dfs_bin_search(V, L):
    def dfs(G, mini, s, t):
        n = len(G)
        visited = [False for _ in range(n)]
        stack = [s]
        while stack:
            u = stack.pop()
            if u == t:
                return True
            visited[u] = True
            for (v, w) in G[u]:
                if w >= mini and not visited[v]:
                    stack.append(v)
        return False

    def bin_search(T, G, s, t):
        l, r = 0, len(T) - 1
        while l <= r:
            mid = (l + r) // 2
            result = dfs(G, T[mid], s, t)
            if not result:
                r = mid - 1
            else:
                l = mid + 1
        if r < len(T):
            return T[r]
        return -1

    G = create_graph(V, L)

    s, t = 0, 1
    n = len(G)
    edges = sorted([e[2] for e in L])

    return bin_search(edges, G, s, t)


def wrapper_dfs_bin_search(V, L):
    result = dfs_bin_search(V, L)
    return result


runtests(wrapper_dfs_bin_search)
