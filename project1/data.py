from testy import *
import dimacs


def dimacs_to_problem(path):
  args = dimacs.loadWeightedGraph(path)
  solution = dimacs.readSolution(path)
  vals = tuple(map(int, solution.split(",")))
  return dict(arg=args, hint=vals)

problems = [

# Optimal path: 1 2 3
{"arg": [3, [
    (1, 2, 2),
    (2, 3, 5),
  ]],
  "hint": (1, 7)},


# Optimal path: 1 3 4
{"arg": [4, [
  (3, 1, 2),
  (3, 2, 4),
  (3, 4, 1),
  ]],
  "hint": (1, 3)},


# Optimal path: 1 3 4 5
{"arg": [6, [
  (1, 3, 1),
  (2, 3, 2),
  (3, 4, 5),
  (4, 5, 1),
  (4, 6, 3),
  ]],
  "hint": (2, 7)},


# Optimal path: 4 1 3 2 5
{"arg": [6, [
  (1, 2, 3),
  (2, 3, 1),
  (1, 3, 1),
  (1, 4, 1),
  (3, 6, 8),
  (2, 5, 3),
  ]],
  "hint": (2, 6)},


# Optimal path: 2 1 3
{"arg": [6, [
  (1, 2, 2),
  (1, 3, 3),
  (1, 4, 4),
  (1, 5, 5),
  (1, 6, 6),
  ]],
  "hint": (1, 5)},


# Optimal path: 2 1 3 etc
{"arg": [6, [
  (1, 2, 1),
  (1, 3, 2),
  (1, 4, 2),
  (1, 5, 2),
  (1, 6, 2),
  ]],
  "hint": (1, 3)},


# Optimal path: 1 2 3 4 6
{"arg": [7, [
  (1, 2, 2),
  (2, 3, 3),
  (3, 4, 5),
  (4, 6, 1),
  (4, 5, 2),
  (4, 7, 3),
  ]],
  "hint": (3, 11)},


# Optimal path: 13 4 11 1 8 3 10
{"arg": [13, [
  (1, 5, 3),
  (1, 6, 8),
  (5, 6, 1),
  (5, 2, 5),
  (6, 2, 2),
  (2, 7, 3),
  (1, 8, 4),
  (1, 9, 3),
  (8, 9, 5),
  (8, 3, 1),
  (9, 3, 7),
  (3, 10, 2),
  (1, 11, 3),
  (1, 12, 2),
  (11, 12, 4),
  (11, 4, 1),
  (12, 4, 6),
  (4, 13, 2),
  ]],
  "hint": (3, 13)},


# Optimal path: 7 2 4 3 8
{"arg": [10, [
  (1, 2, 2),
  (1, 3, 3),
  (1, 4, 2),
  (1, 5, 6),
  (2, 3, 3),
  (2, 4, 1),
  (2, 5, 1),
  (3, 4, 1),
  (3, 5, 1),
  (4, 5, 4),
  (1, 6, 7),
  (2, 7, 4),
  (3, 8, 3),
  (4, 9, 5),
  (5, 10, 6),
  ]],
  "hint": (2, 9)},


# Optimal path: 14 13 11 12 4 3 2 6
{"arg": [16, [
  (1, 2, 2),
  (2, 3, 2),
  (3, 4, 1),
  (4, 5, 4),
  (5, 1, 1),
  (4, 2, 8),
  (2, 6, 3),
  (6, 7, 8),
  (2, 7, 9),
  (3, 15, 7),
  (3, 16, 9),
  (4, 8, 8),
  (8, 9, 2),
  (8, 10, 1),
  (9, 10, 5),
  (4, 11, 6),
  (4, 12, 2),
  (11, 12, 1),
  (11, 13, 1),
  (12, 13, 5),
  (13, 14, 3),
  ]],
  "hint": (3, 13)},


# Optimal path: 14 12 11 15 5 6 7 8
{"arg": [19, [
  (1,2, 3),
  (2,3, 5), (3,4, 1), (2,4, 3), (3,5, 6), (4,5, 9),
  (5,6, 1), (6,7, 5), (5,7, 8),
  (7,8, 5), (7,9, 11), (8,9, 7),
  (5,10, 7), (10,11, 3), (11,15, 2), (5,15, 3), (10,15, 8),
  (11,12, 13),
  (12,13, 5), (13,14, 2), (12,14, 2),
  (15,16, 7), (15,17, 7), (16,17, 4), (16,18, 5), (17,18, 6),
  (18,19, 13)
  ]],
  "hint": (4, 31)},


# Optimal path: 3 2 1 28 29 30
{"arg": [37, [
  (1, 27, 7),
  (1, 28, 6),
  (1, 11, 8),
  (1, 6, 5),
  (1, 2, 4),
  (2, 7, 8),
  (2, 6, 4),
  (2, 4, 6),
  (2, 3, 2),
  (3, 5, 7),
  (3, 4, 3),
  (4, 5, 4),
  (6, 7, 4),
  (7, 9, 4),
  (7, 8, 5),
  (8, 10, 2),
  (8, 9, 3),
  (9, 10, 3),
  (11, 28, 8),
  (11, 27, 7),
  (11, 25, 2),
  (11, 21, 4),
  (11, 19, 3),
  (11, 20, 6),
  (11, 18, 5),
  (11, 16, 2),
  (11, 17, 5),
  (11, 15, 7),
  (11, 13, 4),
  (11, 14, 8),
  (11, 12, 5),
  (12, 14, 8),
  (12, 13, 3),
  (15, 17, 5),
  (15, 16, 3),
  (18, 20, 2),
  (18, 19, 8),
  (21, 26, 4),
  (21, 25, 5),
  (21, 23, 8),
  (21, 24, 5),
  (21, 22, 8),
  (22, 24, 6),
  (22, 23, 3),
  (25, 26, 4),
  (28, 36, 5),
  (28, 35, 6),
  (28, 33, 2),
  (28, 29, 4),
  (29, 34, 3),
  (29, 33, 4),
  (29, 31, 7),
  (29, 30, 3),
  (30, 32, 6),
  (30, 31, 4),
  (31, 32, 4),
  (33, 34, 6),
  (35, 37, 4),
  (35, 36, 5),
  (36, 37, 2),
  ]],
"hint": (4, 19)},
]


graph_files = [
  "sun-small", "sun-med", "sun-large", "sun-huge", "sun-flares", "griddy",
  "octopuss-small", "octopuss-med", "octopuss-large", "octopuss-huge",
  "hectopuss",
  "tree1", "tree2", "tree3", "tree4", "tree5",
  "random-tree1", "random-tree2", "random-tree3", "random-tree4",
  "random-tree5", "random-tree6",
  "true-tree1", "true-tree2", "true-tree3",
  "pasted-grids", "pasted-grids2", "pasted-cliques", "pasted-cliques2"
]

problems += [dimacs_to_problem(f"graphs/{name}") for name in graph_files]

def printarg(N, streets):
    print(f"{N} placy, {len(streets)} ulic")

def printhint(hint):
    print("Wynik: {}".format(hint))

def printsol(sol):
    print("Uzyskany wynik: {}".format(sol))

def check(N, streets, hint, sol):
    if hint == sol:
        print("Test zaliczony")
        return True
    else:
        print("NIEZALICZONY!")
        return False

def runtests(f):
    internal_runtests(printarg, printhint, printsol, check, problems, f)
