from engine.utils import *
from engine.algorithms.uninformed.best_first_graph_search import *


class astar_search:

    def astar_search(problem, h=None, display=False):
        """A* search is best-first graph search with f(n) = g(n)+h(n).
        You need to specify the h function when you call astar_search, or
        else in your Problem subclass."""
        h = memoize(h or problem.h, 'h')
        return best_first_graph_search(problem, lambda n: n.path_cost + h(n), display)
