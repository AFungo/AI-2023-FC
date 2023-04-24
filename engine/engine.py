from enum import Enum, auto

from engine.algorithms.informed.astar_search import AstarSearch
from engine.algorithms.informed.best_first_graph_search import BestFirstGraphSearch
from engine.algorithms.uninformed.breadth_first_search import BreadthFirstSearch
from engine.algorithms.uninformed.depth_first_search import DepthFirstSearch
from engine.problems.practica_1.missionary_and_cannibals_problem import MissionariesAndCannibalsProblem
from engine.problems.practica_1.n_puzzle import NPuzzle
from engine.problems.practica_1.n_queeens import NQueensProblem
from engine.problems.practica_1.romania_map import RomaniaMap
from engine.problems.problem import Problem
from engine.algorithms.search_algorithm import SearchAlgorithm


class Engine:
    def __init__(self, problem, algorithm, initial_state, goal_state=None):
        self.problem = ProblemFactory.create(problem, initial_state, goal_state)
        self.algorithm = AlgorithmFactory.create(algorithm)

    def solve(self):
        node_solution = self.algorithm.search(self.problem)
        return node_solution.solution()


class ProblemFactory:
    def create(self, problem, initial_state, goal_state=None):

        if problem == Problems.ROMANIA_MAP:
            return RomaniaMap(initial_state, goal_state)
        elif problem == Problems.N_PUZZLE:
            return NPuzzle(initial_state, goal_state)
        elif problem == Problems.N_QUEENS:
            return NQueensProblem(initial_state)
        elif problem == Problems.CANNIBALS_AND_MISSIONARIES:
            return MissionariesAndCannibalsProblem(initial_state)


class AlgorithmFactory:

    def __init__(self, algorithm, heuristic=None):
        self.algorithm = algorithm
        self.heuristic = heuristic

    def create(self):
        if InformedAlgorithms.__contains__(self.algorithm):
            return self.create_informed_algorithm(self.algorithm, self.heuristic)
        elif UninformedAlgorithms.__contains__(self.algorithm):
            return self.create_uninformed_algorithm(self.algorithm)
        Exception("Algorithm type not supported")

    def create_informed_algorithm(self, algorithm, problem, heuristic, display):
        if algorithm == InformedAlgorithms.ASTAR_SEARCH:
            return AstarSearch(problem, heuristic, display)
        elif algorithm == InformedAlgorithms.BEST_FIRST_GRAPH_SEARCH:
            return BestFirstGraphSearch(problem, heuristic, display)

    def create_uninformed_algorithm(self, algorithm):
        if algorithm == UninformedAlgorithms.BREADTH_FIRST_SEARCH:
            return BreadthFirstSearch()
        elif algorithm == UninformedAlgorithms.DEPTH_FIRST_SEARCH:
            return DepthFirstSearch()
        elif algorithm == UninformedAlgorithms.BREADTH_FIRST_GRAPH_SEARCH:
            return BreadthFirstGraphSearch()
        elif algorithm == UninformedAlgorithms.DEPTH_FIRST_GRAPH_SEARCH:
            return DepthFirstGraphSearch()


class Problems(Enum):
    ROMANIA_MAP = auto()
    N_PUZZLE = auto()
    N_QUEENS = auto()
    CANNIBALS_AND_MISSIONARIES = auto()


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