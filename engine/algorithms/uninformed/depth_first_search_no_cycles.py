from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.problems.problem import Problem
from engine.node import Node


class DepthFirstSearchNoCycles(SearchAlgorithm):

    def __init__(self, problem):
        self.problem = problem

    def search(self):
        frontier = [Node(self.problem.initial_state())]
        while frontier:
            node = frontier.pop()
            if self.problem.goal_test(node.state):
                Exception("limited")
            path_states = list(map(lambda l: l.state, node.path()))
            if path_states.count(node.state) < 2:
                frontier.extend(node.expand(self.problem))
        return None
