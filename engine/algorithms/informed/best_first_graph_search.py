from engine.problems.problem import Problem
from engine.utils import *
from engine.node import *


class BestFirstGraphSearch:
    def __init__(self, problem, heuristic):
        self.problem = problem
        self.heuristic = heuristic

    def search(self):
        """Search the nodes with the lowest f scores first.
        You specify the function f(node) that you want to minimize; for example,
        if f is a heuristic estimate to the goal, then we have greedy best
        first search; if f is node.depth then we have breadth-first search.
        There is a subtlety: the line "f = memoize(f, 'f')" means that the f
        values will be cached on the nodes as they are computed. So after doing
        a best first search you can examine the f values of the path returned."""
        self.heuristic = memoize(self.heuristic, 'f')
        node = Node(self.problem.initial)
        frontier = PriorityQueue('min', self.heuristic)
        frontier.append(node)
        explored = set()
        while frontier:
            node = frontier.pop()
            if self.problem.goal_test(node.state):
                return node
            explored.add(node.state)
            for child in node.expand(self.problem):
                if child.state not in explored and child not in frontier:
                    frontier.append(child)
                elif child in frontier:
                    if self.heuristic(child) < frontier[child]:
                        del frontier[child]
                        frontier.append(child)
        return None
