from dimacs import loadDirectedWeightedGraph, readSolution
from stoer_wagner import stoer_wagner
from min_cut_flow import min_cut_flow
import unittest


class StoerWagnerTest(unittest.TestCase):
    @staticmethod
    def get_data(path):
        V, L = loadDirectedWeightedGraph(path)
        expected = int(readSolution(path))
        result = stoer_wagner(V, L)
        return expected, result

    def test_stoerwagner_clique5(self, path="graphs-lab3/clique5"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_clique20(self, path="graphs-lab3/clique20"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_clique100(self, path="graphs-lab3/clique100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_clique200(self, path="graphs-lab3/clique200"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_cycle(self, path="graphs-lab3/cycle"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_geo20_2b(self, path="graphs-lab3/geo20_2b"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_geo20_2c(self, path="graphs-lab3/geo20_2c"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_geo100_2a(self, path="graphs-lab3/geo100_2a"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_grid5x5(self, path="graphs-lab3/grid5x5"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_grid100x100(self, path="graphs-lab3/grid100x100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_mc1(self, path="graphs-lab3/mc1"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_mc2(self, path="graphs-lab3/mc2"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_path(self, path="graphs-lab3/path"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_rand20_100(self, path="graphs-lab3/rand20_100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_rand100_500(self, path="graphs-lab3/rand100_500"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_simple(self, path="graphs-lab3/simple"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_stoerwagner_trivial(self, path="graphs-lab3/trivial"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

"""
class EdgeConnectivityTest(unittest.TestCase):
    @staticmethod
    def get_data(path):
        V, L = loadDirectedWeightedGraph(path)
        expected = int(readSolution(path))
        result = min_cut_flow(V, L)
        return expected, result

    def test_edgeconnectivity_clique5(self, path="graphs-lab3/clique5"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_edgeconnectivity_clique20(self, path="graphs-lab3/clique20"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_edgeconnectivity_clique100(self, path="graphs-lab3/clique100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_edgeconnectivity_clique200(self, path="graphs-lab3/clique200"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_edgeconnectivity_cycle(self, path="graphs-lab3/cycle"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_edgeconnectivity_geo20_2b(self, path="graphs-lab3/geo20_2b"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_edgeconnectivity_geo20_2c(self, path="graphs-lab3/geo20_2c"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_edgeconnectivity_geo100_2a(self, path="graphs-lab3/geo100_2a"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_edgeconnectivity_grid5x5(self, path="graphs-lab3/grid5x5"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    #def test_edgeconnectivity_grid100x100(self, path="graphs-lab3/grid100x100"):
    #    e, r = self.get_data(path)
    #    self.assertEqual(r, e)

    def test_edgeconnectivity_mc1(self, path="graphs-lab3/mc1"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_edgeconnectivity_mc2(self, path="graphs-lab/mc2"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_edgeconnectivity_path(self, path="graphs-lab3/path"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_edgeconnectivity_rand20_100(self, path="graphs-lab3/rand20_100"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_edgeconnectivity_rand100_500(self, path="graphs-lab3/rand100_500"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_edgeconnectivity_simple(self, path="graphs-lab3/simple"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)

    def test_edgeconnectivity_trivial(self, path="graphs-lab3/trivial"):
        e, r = self.get_data(path)
        self.assertEqual(r, e)
"""

if __name__ == '__main__':
    unittest.main()

