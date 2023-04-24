from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.node import Node


class DepthFirstGraphSearch(SearchAlgorithm):

    def __init__(self, problem):
        self.problem = problem

    def search(self):
        frontier = [(Node(self.problem.initial))]  # Stack

        explored = set()
        while frontier:
            node = frontier.pop()
            if self.problem.goal_test(node.state):
                return node
            explored.add(node.state)
            frontier.extend(child for child in node.expand(self.problem)
                            if child.state not in explored and child not in frontier)
        return None
