import os
import unittest
from dimacs import loadWeightedGraph, readSolution
from lexBFS import lexBFS, chordal, max_clique, coloring, vertex_cover, make_graph


class LexBFSTest(unittest.TestCase):
    def test_lexBFS(self):
        for root, dirs, file in os.walk("graphs-lab4/chordal"):
            for f in file:
                with self.subTest(f=f):
                    V, L = loadWeightedGraph("graphs-lab4/chordal/"+f)
                    G = make_graph(V, L)
                    self.assertEqual(checkLexBFS(G, lexBFS(G)), True)


class ChordalTest(unittest.TestCase):
    def test_chordal(self):
        for root, dirs, file in os.walk("graphs-lab4/chordal"):
            for f in file:
                with self.subTest(f=f):
                    V, L = loadWeightedGraph("graphs-lab4/chordal/"+f)
                    result = chordal(V, L)
                    sol = True
                    if int(readSolution("graphs-lab4/chordal/"+f)) == 0:
                        sol = False
                    self.assertEqual(result, sol)


class MaxCliqueTest(unittest.TestCase):
    def test_max_clique(self):
        for root, dirs, file in os.walk("graphs-lab4/maxclique"):
            for f in file:
                with self.subTest(f=f):
                    V, L = loadWeightedGraph("graphs-lab4/maxclique/"+f)
                    sol = int(readSolution("graphs-lab4/maxclique/"+f))
                    self.assertEqual(max_clique(V, L), sol)


class ColoringTest(unittest.TestCase):
    def test_coloring(self):
        for root, dirs, file in os.walk("graphs-lab4/coloring"):
            for f in file:
                with self.subTest(f=f):
                    V, L = loadWeightedGraph("graphs-lab4/coloring/"+f)
                    sol = int(readSolution("graphs-lab4/coloring/"+f))
                    self.assertEqual(coloring(V, L), sol)


class VertexCoverTest(unittest.TestCase):
    def test_vertex_cover(self):
        for root, dirs, file in os.walk("graphs-lab4/vcover"):
            for f in file:
                with self.subTest(f=f):
                    V, L = loadWeightedGraph("graphs-lab4/vcover/"+f)
                    sol = int(readSolution("graphs-lab4/vcover/"+f))
                    self.assertEqual(vertex_cover(V, L), sol)


def checkLexBFS(G, vs):
    n = len(G)
    pi = [None] * n
    for i, v in enumerate(vs):
        pi[v] = i

    for i in range(n-1):
        for j in range(i+1, n-1):
            Ni = G[vs[i]].out
            Nj = G[vs[j]].out

            verts = [pi[v] for v in Nj - Ni if pi[v] < i]
            if verts:
                viable = [pi[v] for v in Ni - Nj]
                if not viable or min(verts) <= min(viable):
                    return False
    return True


if __name__ == "__main__":
    unittest.main()
