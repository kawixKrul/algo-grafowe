import os
import time
import unittest
from typing import Tuple
from dimacs import loadWeightedGraph

test_case = {}
path = "../graphs-lab1"
V: int  # Liczba wierzchołków
L: Tuple[int, int, int]  # List krawędzi


def create_graph(V: int, L: Tuple[int, int, int]):
    graph = [[] for _ in range(V)]

    for (x, y, c) in L:
        graph[x - 1].append([y - 1, c])
        graph[y - 1].append([x - 1, c])

    return graph


def runtests(func):
    times = []
    passed = []
    with open("tests.txt") as tests:
        for i, line in enumerate(tests.readlines()):
            graph, expected = line.split(" ")
            V, L = loadWeightedGraph(path+"/"+graph)
            start = time.time()
            result = func(V, L)
            elapsed_time = time.time() - start
            try:
                assert result == int(expected)
            except AssertionError:
                passed.append(False)
            else:
                passed.append(True)
            times.append(elapsed_time)
            print(f"""Test nr {i} from {graph}: {"passed" if passed[-1] else "failed"}
expected: {expected}""", end="")
            print(f"""output: {result}
time: {round(times[-1],3)} seconds\n""")

    print(f"""Total passed: {sum(1 if p else 0 for p in passed)}/{len(passed)}
Total time: {round(sum(times),3)} seconds""")


if __name__ == "__main__":
    if not os.path.exists("tests.txt"):
        for root, dirs, file in os.walk(path):
            for f in file:
                test_case[f] = int(open(path+"/"+f).readlines()[0].split(" ")[-1].strip())

        with open("tests.txt", "w") as f:
            for key, value in test_case.items():
                f.write(f"{key} {value}\n")


