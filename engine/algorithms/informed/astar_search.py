from engine.utils import *
from engine.algorithms.informed.best_first_graph_search import BestFirstGraphSearch


class AstarSearch:

    def __init__(self, problem, heuristic=None):
        self.problem = problem
        self.heuristic = heuristic

    def search(self):
        self.heuristic = memoize(self.heuristic, 'h')
        return BestFirstGraphSearch(self.problem, lambda n: n.path_cost + self.heuristic(n)).search()
