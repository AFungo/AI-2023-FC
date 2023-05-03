from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.algorithms.uninformed.depth_limited_search import DepthLimitedSearch


class InterativeDeepeningSearch(SearchAlgorithm):

    def __init__(self, problem):
        self.problem = problem

    def search(self):
        while True:
            depth = 0
            result = DepthLimitedSearch(self.problem, depth).search()
            depth += 19
            if result is not None:
                return result
