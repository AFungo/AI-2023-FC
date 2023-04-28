from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.problems.problem import Problem
from engine.node import Node


class DepthLimitedSearch(SearchAlgorithm):

    def __init__(self, problem, depth):
        self.problem = problem
        self.depth = depth

    def search(self):
        frontier = [Node(self.problem.initial_state())]
        while frontier:
            node = frontier.pop()
            if self.problem.goal_test(node.state):
                return node
            path_states = list(map(lambda l: l.state, node.path()))
            if node.depth > self.depth:
                return None
            elif path_states.count(node.state) < 2:
                frontier.extend(node.expand(self.problem))
        return None
