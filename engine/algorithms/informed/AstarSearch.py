from engine.utils import *
from engine.algorithms.informed.BestFirstGraphSearch import BestFirstGraphSearch


class AstarSearch:

    def __init__(self, problem):
        self.problem = problem

    def search(self, h=None, display=False):
        """A* search is best-first graph search with f(n) = g(n)+h(n).
        You need to specify the h function when you call astar_search, or
        else in your Problem subclass."""
        h = memoize(h or self.problem.h, 'h')
        return BestFirstGraphSearch(self.problem, lambda n: n.path_cost + h(n)).search(h, display)
