from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.algorithms.uninformed.best_first_search import BestFirstSearch


class UniformCostSearch(SearchAlgorithm):
    def __init__(self, problem):
        self.problem = problem

    def search(self):
        bfs = BestFirstSearch(self.problem, lambda n: n.path_cost)
        return bfs.search()
