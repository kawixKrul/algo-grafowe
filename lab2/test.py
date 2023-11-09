from typing import Any
from dimacs import loadDirectedWeightedGraph
import unittest
import time
from flow_list import FordFulkerson_List
from flow_matrix import FordFulkerson_Matrix
from searches import BFS_list, DFS_list, BFS_matrix, DFS_matrix


PATH_FLOW = "graphs-lab2/flow/"
PATH_CONNECTIVITY = "graphs-lab2/connectivity/"
TIME_LIMIT = 10


class FlowTestListBFS(unittest.TestCase):
    @staticmethod
    def get_data(path):
        expected = int(open(path).readlines()[0].split("=")[-1].strip())
        V, L = loadDirectedWeightedGraph(path)
        Graph = convert_list(convert_matrix(V, L))
        result = FordFulkerson_List(Graph, 0, V - 1, BFS_list)
        return expected, result

    def test_ford_clique5(self, path=PATH_FLOW+"clique5"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_clique20(self, path=PATH_FLOW+"clique20"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_clique100(self, path=PATH_FLOW+"clique100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_grid5x5(self, path=PATH_FLOW+"grid5x5"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    """def test_ford_grid100x100(self, path=PATH_FLOW+"grid100x100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)"""

    def test_ford_pp100(self, path=PATH_FLOW+"pp100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_rand20_100(self, path=PATH_FLOW+"rand20_100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_rand100_500(self, path=PATH_FLOW+"rand100_500"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_simple(self, path=PATH_FLOW+"simple"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_simple2(self, path=PATH_FLOW+"simple2"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_trivial(self, path=PATH_FLOW+"trivial"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_trivial2(self, path=PATH_FLOW+"trivial2"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_worstcase(self, path=PATH_FLOW+"worstcase"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

class FlowTestMatrixBFS(unittest.TestCase):
    @staticmethod
    def get_data(path):
        expected = int(open(path).readlines()[0].split("=")[-1].strip())
        V, L = loadDirectedWeightedGraph(path)
        Graph = convert_matrix(V, L)
        result = FordFulkerson_Matrix(Graph, 0, V - 1, BFS_matrix)
        return expected, result

    def test_ford_clique5(self, path=PATH_FLOW+"clique5"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_clique20(self, path=PATH_FLOW+"clique20"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_clique100(self, path=PATH_FLOW+"clique100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_grid5x5(self, path=PATH_FLOW+"grid5x5"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    """def test_ford_grid100x100(self, path=PATH_FLOW+"grid100x100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)"""

    def test_ford_pp100(self, path=PATH_FLOW+"pp100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_rand20_100(self, path=PATH_FLOW+"rand20_100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_rand100_500(self, path=PATH_FLOW+"rand100_500"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_simple(self, path=PATH_FLOW+"simple"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_simple2(self, path=PATH_FLOW+"simple2"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_trivial(self, path=PATH_FLOW+"trivial"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_trivial2(self, path=PATH_FLOW+"trivial2"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_worstcase(self, path=PATH_FLOW+"worstcase"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)


class FlowTestListDFS(unittest.TestCase):
    @staticmethod
    def get_data(path):
        expected = int(open(path).readlines()[0].split("=")[-1].strip())
        V, L = loadDirectedWeightedGraph(path)
        Graph = convert_list(convert_matrix(V, L))
        result = FordFulkerson_List(Graph, 0, V - 1, DFS_list)
        return expected, result

    def test_ford_clique5(self, path=PATH_FLOW+"clique5"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_clique20(self, path=PATH_FLOW+"clique20"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_clique100(self, path=PATH_FLOW+"clique100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_grid5x5(self, path=PATH_FLOW+"grid5x5"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    """def test_ford_grid100x100(self, path=PATH_FLOW+"grid100x100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)"""

    def test_ford_pp100(self, path=PATH_FLOW+"pp100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_rand20_100(self, path=PATH_FLOW+"rand20_100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_rand100_500(self, path=PATH_FLOW+"rand100_500"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_simple(self, path=PATH_FLOW+"simple"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_simple2(self, path=PATH_FLOW+"simple2"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_trivial(self, path=PATH_FLOW+"trivial"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_trivial2(self, path=PATH_FLOW+"trivial2"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_worstcase(self, path=PATH_FLOW+"worstcase"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)


class FlowTestMatrixDFS(unittest.TestCase):
    @staticmethod
    def get_data(path):
        expected = int(open(path).readlines()[0].split("=")[-1].strip())
        V, L = loadDirectedWeightedGraph(path)
        Graph = convert_matrix(V, L)
        result = FordFulkerson_Matrix(Graph, 0, V - 1, DFS_matrix)
        return expected, result

    def test_ford_clique5(self, path=PATH_FLOW+"clique5"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_clique20(self, path=PATH_FLOW+"clique20"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_clique100(self, path=PATH_FLOW+"clique100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_grid5x5(self, path=PATH_FLOW+"grid5x5"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    """def test_ford_grid100x100(self, path=PATH_FLOW+"grid100x100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)"""

    def test_ford_pp100(self, path=PATH_FLOW+"pp100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_rand20_100(self, path=PATH_FLOW+"rand20_100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_rand100_500(self, path=PATH_FLOW+"rand100_500"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_simple(self, path=PATH_FLOW+"simple"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_simple2(self, path=PATH_FLOW+"simple2"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_trivial(self, path=PATH_FLOW+"trivial"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_trivial2(self, path=PATH_FLOW+"trivial2"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_ford_worstcase(self, path=PATH_FLOW+"worstcase"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)


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


if __name__ == "__main__":
    unittest.main()




