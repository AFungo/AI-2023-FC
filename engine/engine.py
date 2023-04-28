from enum import Enum, auto

from engine.algorithms.informed.astar_search import AstarSearch
from engine.algorithms.informed.best_first_graph_search import BestFirstGraphSearch
from engine.algorithms.uninformed.breadth_first_graph_search import BreadthFirstGraphSearch
from engine.algorithms.uninformed.breadth_first_search import BreadthFirstSearch
from engine.algorithms.uninformed.depth_first_graph_search import DepthFirstGraphSearch
from engine.algorithms.uninformed.depth_first_search import DepthFirstSearch
from engine.algorithms.uninformed.depth_limited_search import DepthLimitedSearch
from engine.problems.practica_1.missionary_and_cannibals_problem import MissionariesAndCannibalsProblem
from engine.problems.practica_1.n_puzzle import NPuzzle
from engine.problems.practica_1.n_queeens import NQueensProblem
from engine.problems.practica_1.romania_map import RomaniaMap
from engine.problems.practica_1.n_puzzle import NPuzzleHeuristics
from engine.problems.practica_1.n_queeens import NQueensHeuristics
from engine.problems.practica_1.romania_map import RomaniaMapHeuristics
from engine.problems.problem import Problem
from engine.algorithms.search_algorithm import SearchAlgorithm


class Engine:
    def __init__(self, problem, algorithm, initial_state, goal_state=None, heuristic=None, algorithm_params=None):
        self.problem = ProblemFactory(problem, initial_state, goal_state).create
        self.heuristic = HeuristicFactory(problem, heuristic).create()
        algorithm_factory = AlgorithmFactory(algorithm, problem, heuristic, params=algorithm_params)
        self.algorithm = algorithm_factory.create()
        self.initial_state = initial_state
        self.goal_state = goal_state

    def solve(self):
        node_solution = self.algorithm.search()
        return node_solution.solution()


class ProblemFactory:

    def __init__(self, problem, initial_state, goal_state=None):
        self.problem = problem
        self.initial_state = initial_state
        self.goal_state = goal_state

    def create(self):
        if self.problem == Problems.ROMANIA_MAP:
            return RomaniaMap(self.initial_state, self.goal_state)
        elif self.problem == Problems.N_PUZZLE:
            return NPuzzle(self.initial_state, self.goal_state)
        elif self.problem == Problems.N_QUEENS:
            return NQueensProblem(self.initial_state)
        elif self.problem == Problems.CANNIBALS_AND_MISSIONARIES:
            return MissionariesAndCannibalsProblem(self.initial_state)
        Exception("Problem type not supported")


class HeuristicFactory:

    def __init__(self, problem, heuristic):
        self.problem = problem
        self.heuristic = heuristic

    def create(self):
        if self.heuristic is None:
            return None

        if self.problem == Problems.N_PUZZLE:
            if self.heuristic == Heuristic.MANHATTAN:
                return NPuzzleHeuristics().manhattan_heuristic
            elif self.heuristic == Heuristic.MISPLACED_NUMBERS:
                return NPuzzleHeuristics().misplaced_numbers
            elif self.heuristic == Heuristic.GASCHNIG:
                return NPuzzleHeuristics().gaschnig
        elif self.problem == Problems.N_QUEENS:
            if self.heuristic == Heuristic.UNATTACHED_SQUARES:
                return NQueensHeuristics.unattacked_squares
        elif self.problem == Problems.ROMANIA_MAP:
            if self.heuristic == Heuristic.STRAIGTH_LINE_DISTANCE:
                return RomaniaMapHeuristics.straigth_line_distance
        Exception("Problem or Heuristic type not supported")


class AlgorithmFactory:

    def __init__(self, algorithm, problem, heuristic=None, params=None):
        if params is None:
            self.params = {}
        else:
            self.params = params
        self.algorithm = algorithm
        self.problem = problem
        self.heuristic = heuristic

    def create(self):
        if InformedAlgorithms.__contains__(self.algorithm):
            return self.create_informed_algorithm()
        elif UninformedAlgorithms.__contains__(self.algorithm):
            return self.create_uninformed_algorithm()
        Exception("Algorithm type not supported")

    def create_informed_algorithm(self):
        if self.algorithm == InformedAlgorithms.ASTAR_SEARCH:
            return AstarSearch(self.problem, self.heuristic)
        elif self.algorithm == InformedAlgorithms.BEST_FIRST_GRAPH_SEARCH:
            return BestFirstGraphSearch(self.problem, self.heuristic)
        Exception("Algorithm type not supported")

    def create_uninformed_algorithm(self):
        if self.algorithm == UninformedAlgorithms.BREADTH_FIRST_SEARCH:
            return BreadthFirstSearch(self.problem)
        elif self.algorithm == UninformedAlgorithms.DEPTH_FIRST_SEARCH:
            return DepthFirstSearch(self.problem)
        elif self.algorithm == UninformedAlgorithms.BREADTH_FIRST_GRAPH_SEARCH:
            return BreadthFirstGraphSearch(self.problem)
        elif self.algorithm == UninformedAlgorithms.DEPTH_FIRST_GRAPH_SEARCH:
            return DepthFirstGraphSearch(self.problem)
        elif self.algorithm == UninformedAlgorithms.DEPTH_LIMITED_SEARCH:
            if 'depth_limit' not in self.params:
                Exception("Depth limit not specified")
            return DepthLimitedSearch(self.problem, self.params['depth_limit'])
        Exception("Algorithm type not supported")


class Problems(Enum):
    ROMANIA_MAP = auto()
    N_PUZZLE = auto()
    N_QUEENS = auto()
    CANNIBALS_AND_MISSIONARIES = auto()


class Heuristic(Enum):
    UNATTACHED_SQUARES = auto()
    MANHATTAN = auto()
    MISPLACED_NUMBERS = auto()
    GASCHNIG = auto()
    STRAIGTH_LINE_DISTANCE = auto()


class AlgorithmsType(Enum):
    INFORMED = auto()
    UNINFORMED = auto()


class InformedAlgorithms(Enum):
    BEST_FIRST_GRAPH_SEARCH = auto()
    ASTAR_SEARCH = auto()


class UninformedAlgorithms(Enum):
    DEPTH_FIRST_GRAPH_SEARCH = auto()
    DEPTH_FIRST_SEARCH = auto()
    BREADTH_FIRST_GRAPH_SEARCH = auto()
    BREADTH_FIRST_SEARCH = auto()
    DEPTH_LIMITED_SEARCH = auto()
