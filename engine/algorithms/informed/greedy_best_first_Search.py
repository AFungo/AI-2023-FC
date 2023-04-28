from engine.problems.problem import Problem
from engine.utils import *
from engine.node import *
from engine.algorithms.informed.best_first_graph_search import BestFirstGraphSearch


class GreedyBestFirstSearch:

    def __init__(self, problem, heuristic):
        self.problem = problem
        self.heuristic = heuristic

    def search(self):
        return BestFirstGraphSearch(self.problem, self.heuristic)
