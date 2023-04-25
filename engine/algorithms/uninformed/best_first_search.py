from engine.algorithms.search_algorithm import SearchAlgorithm
import heapq

from engine.node import Node


class BestFirstSearch(SearchAlgorithm):
    def __init__(self, problem, function):
        self.problem = problem
        self.function = function

    def search(self):
        initial = self.problem.initial_state()
        node = Node(state=initial)
        frontier = []
        heapq.heappush(frontier, (self.function(node), node))
        reached = {node.state: node}
        while not len(frontier) == 0:
            node = heapq.heappop(frontier)[1]
            if self.problem.goal_test(node.state):
                return node
            for child in node.expand(self.problem):
                if child.state not in reached or child.path_cost < reached[child.state].path_cost:
                    heapq.heappush(frontier, (self.function(child), child))
                    reached[child.state] = child
        return None
