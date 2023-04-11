from engine.problems.problem import Problem
from engine.algorithms.search_algorithm import SearchAlgorithm


class Engine:
    def __init__(self, problem, algorithm):
        self.problem = problem
        self.algorithm = algorithm

    # def solve(self) -> Solution:
    #     node_solution = self.algorithm.search(self.problem)
    #     return node_solution.solution()
