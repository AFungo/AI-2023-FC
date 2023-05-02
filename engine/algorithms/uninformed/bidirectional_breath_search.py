import heapq

from engine.algorithms.search_algorithm import SearchAlgorithm
from engine.node import Node
from engine.utils import join_nodes


class BidirectionalBreathSearch(SearchAlgorithm):
    def __init__(self, initial_problem, final_problem,initial_function, goal_function):
        self.initial_state = initial_problem.initial_state()
        self.goal_state = final_problem.initial_state()
        self.initial_function = initial_function
        self.goal_function = goal_function
        self.initial_problem = initial_problem
        self.final_problem = final_problem

    def search(self):

        if self.initial_state == self.goal_state:
            return Node(self.initial_state)

        node_initial = Node(self.initial_state)
        node_goal = Node(self.goal_state)

        frontier_initial = []
        frontier_goal = []

        heapq.heappush(frontier_initial, (self.initial_function(node_initial), node_initial))
        heapq.heappush(frontier_goal, (self.goal_function(node_initial), node_goal))

        reached_initial = {node_initial.state: node_initial}
        reached_goal = {node_goal.state: node_goal}

        solution = None

        while not self.terminated(solution, frontier_initial, frontier_goal):
            initial_min_node = self.initial_function(heapq.nsmallest(1, frontier_initial)[0][1])
            goal_min_node = self.goal_function(heapq.nsmallest(1, frontier_goal)[0][1])

            if initial_min_node < goal_min_node:
                solution = self.proceed(True, self.initial_problem, frontier_initial, reached_initial, self.initial_function, reached_goal, solution)
            else:
                solution = self.proceed(False, self.final_problem, frontier_goal, reached_goal, self.goal_function, reached_initial, solution)

        return solution

    def proceed(self, direction, problem, frontier, reached, function, reached_opposite, solution):
        node = heapq.heappop(frontier)[1]
        for child in node.expand(problem):
            state = child.state
            if state not in reached or child.path_cost < reached[child.state].path_cost:
                heapq.heappush(frontier, (function(child), child))
                reached[state] = child
            if child.state in reached_opposite:
                op = reached_opposite[child.state]
                new_solution = join_nodes(direction, child, op)#child.path() + reached_opposite[child.state].path()[::-1]
                if solution is None or new_solution.path_cost < solution.path_cost:
                    solution = new_solution
        return solution

    def terminated(self, solution, frontier_initial, frontier_goal):
        return len(frontier_initial) == 0 or len(frontier_goal) == 0 or solution is not None
