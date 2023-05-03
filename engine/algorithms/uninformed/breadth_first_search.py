from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.node import Node
from collections import deque


class BreadthFirstSearch(SearchAlgorithm):

    def __init__(self, problem):
        self.problem = problem

    def search(self):
        frontier = deque([Node(self.problem.initial_state())])  # FIFO queue
        while frontier:
            node = frontier.popleft()
            if self.problem.goal_test(node.state):
                return node
            frontier.extend(node.expand(self.problem))
        return None
