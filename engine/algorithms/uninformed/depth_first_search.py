from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.node import Node


class DepthFirstSearch(SearchAlgorithm):

    def __init__(self, problem):
        self.problem = problem

    def search(self):
        frontier = [Node(self.problem.initial_state())]
        while frontier:
            node = frontier.pop()
            if self.problem.goal_test(node.state):
                return node
            frontier.extend(node.expand(self.problem))
        return None

