from engine.utils import *
from engine.algorithms.informed.best_first_graph_search import BestFirstGraphSearch


class AstarSearch:

    def __init__(self, problem, h=None):
        self.problem = problem
        self.h = h

    def search(self):
        self.h = memoize(self.h or self.problem.h, 'h')
        return BestFirstGraphSearch(self.problem, lambda n: n.path_cost + self.h(n)).search()
