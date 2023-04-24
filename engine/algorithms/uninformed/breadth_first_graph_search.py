from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.node import Node
from collections import deque


class BreadthFirstGraphSearch(SearchAlgorithm):
    def __init__(self, problem):
        self.problem = problem

    def search(self):
        """[Figure 3.11]
        Note that this function can be implemented in a
        single line as below:
        return graph_search(problem, FIFOQueue())
        """
        node = Node(self.problem.initial)
        if self.problem.goal_test(node.state):
            return node
        frontier = deque([node])
        explored = set()
        while frontier:
            node = frontier.popleft()
            explored.add(node.state)
            for child in node.expand(self.problem):
                if child.state not in explored and child not in frontier:
                    if self.problem.goal_test(child.state):
                        return child
                    frontier.append(child)
        return None
