from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.node import Node
from collections import deque
from engine.problems.problem import Problem


class BreadthFirstSearch(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        frontier = deque([Node(problem.initial_state())])  # FIFO queue
        while frontier:
            node = frontier.popleft()
            if problem.goal_test(node.state):
                return node
            frontier.extend(node.expand(problem))
        return None

