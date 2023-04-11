from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.problems.problem import Problem
from engine.node import Node


class DepthFirstSearch(SearchAlgorithm):
    def search(self, problem: Problem) -> Node | None:
        frontier = [Node(problem.initial_state())]
        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                return node
            frontier.extend(node.expand(problem))
        return None

