from enum import Enum, auto

from engine.algorithms.informed.astar_search import AstarSearch
from engine.algorithms.informed.best_first_graph_search import BestFirstGraphSearch
from engine.algorithms.informed.greedy_best_first_Search import GreedyBestFirstSearch
from engine.algorithms.uninformed.bidirectional_breath_search import BidirectionalBreathSearch
from engine.algorithms.uninformed.breadth_first_graph_search import BreadthFirstGraphSearch
from engine.algorithms.uninformed.breadth_first_search import BreadthFirstSearch
from engine.algorithms.uninformed.depth_first_graph_search import DepthFirstGraphSearch
from engine.algorithms.uninformed.depth_first_search import DepthFirstSearch
from engine.algorithms.uninformed.depth_limited_search import DepthLimitedSearch
from engine.problems.abstract_problem import CountNodes, CountNodesBidirectional, CountNodesInverted
from engine.problems.practica_1.missionary_and_cannibals_problem import MissionariesAndCannibalsProblem
from engine.problems.practica_1.n_puzzle import NPuzzle
from engine.problems.practica_1.n_queeens import NQueensProblem
from engine.problems.practica_1.romania_map import RomaniaMap, RomaniaMapHeuristics
from engine.problems.practica_1.n_puzzle import NPuzzleHeuristics
from engine.problems.practica_1.n_queeens import NQueensHeuristics
from engine.algorithms.uninformed.uniform_cost_search import UniformCostSearch
from engine.algorithms.uninformed.interative_deepening_search import InterativeDeepeningSearch
from engine.algorithms.search_algorithm import SearchAlgorithm
import time
import psutil

from engine.utils import parse_data_to_dictionary


class Engine:
    def __init__(self, problem, algorithm, problem_params, heuristic=None, algorithm_params=None, heuristic_params=None):
        self.problem_name = problem
        self.algorithm_name = algorithm
        self.problem = ProblemFactory(problem, problem_params).create()
        self.heuristic = HeuristicFactory(problem, heuristic, heuristic_params).create()
        algorithm_factory = AlgorithmFactory(algorithm, self.problem, self.heuristic, params=algorithm_params)
        self.algorithm = algorithm_factory.create()
        self.problem_params = problem_params

    def solve(self):
        process = psutil.Process()
        start_memory = process.memory_info().rss
        start_time = time.time()

        node_solution = self.algorithm.search()

        end_memory = process.memory_info().rss
        end_time = time.time()

        memory_usage = (end_memory - start_memory) / 1024 / 1024
        run_time = round(end_time - start_time, 5)

        return parse_data_to_dictionary(self.problem_name, self.algorithm_name, self.heuristic,
                                        self.problem.initial_state(), node_solution.state.__str__(), node_solution.depth,
                                        self.problem.explored_node, self.problem.generated_nodes, memory_usage, run_time,
                                        node_solution.path_cost, node_solution.path(), node_solution.solution())


class ProblemFactory:

    def __init__(self, problem, problem_params):
        self.problem = problem
        self.problem_params = problem_params

    def create(self):
        if self.problem == Problems.ROMANIA_MAP:
            return CountNodes(RomaniaMap(self.problem_params["initial_state"], self.problem_params["goal_state"]))
        elif self.problem == Problems.NPUZZLE:
            return CountNodes(NPuzzle(self.problem_params["initial_state"]))
        elif self.problem == Problems.N_QUEENS:
            return CountNodes(NQueensProblem(self.problem_params["number_queens"]))
            # return NQueensProblem.__init__(self.initial_state)
        elif self.problem == Problems.CANNIBALS_AND_MISSIONARIES:
            pass
            # return MissionariesAndCannibalsProblem.__init__(self.initial_state)
        Exception("Problem type not supported")


class HeuristicFactory:

    def __init__(self, problem, heuristic, params):
        self.problem = problem
        self.heuristic = heuristic
        self.params = params

    def create(self):
        if self.heuristic is None:
            return None

        if self.problem == Problems.NPUZZLE:
            if self.heuristic == Heuristic.MANHATTAN:
                return NPuzzleHeuristics().manhattan
            elif self.heuristic == Heuristic.MISPLACED_NUMBERS:
                return NPuzzleHeuristics().misplaced_numbers
            elif self.heuristic == Heuristic.GASCHNIG:
                return NPuzzleHeuristics().gaschnig
            elif self.heuristic == Heuristic.LINERAR_CONFLICT:
                return NPuzzleHeuristics().linear_conflict
        elif self.problem == Problems.N_QUEENS:
            if self.heuristic == Heuristic.UNATTACHED_SQUARES:
                return NQueensHeuristics().unattacked_squares
        elif self.problem == Problems.ROMANIA_MAP:
            if self.heuristic == Heuristic.STRAIGTH_LINE_DISTANCE:
                return RomaniaMapHeuristics(self.params["goal_city"]).straigth_line_distance
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
        elif self.algorithm == InformedAlgorithms.GREEDY_BEST_FIRST_SEARCH:
            return GreedyBestFirstSearch(self.problem, self.heuristic)
        Exception("Algorithm type not supported")

    def create_uninformed_algorithm(self):
        if self.algorithm == UninformedAlgorithms.BREADTH_FIRST_SEARCH:
            return BreadthFirstGraphSearch(self.problem)
        elif self.algorithm == UninformedAlgorithms.DEPTH_FIRST_SEARCH:
            return DepthFirstSearch(self.problem)
        elif self.algorithm == UninformedAlgorithms.UNIFORM_COST_SEARCH:
            return UniformCostSearch(self.problem)
        elif self.algorithm == UninformedAlgorithms.ITERATIVE_DEEPENING_SEARCH:
            return InterativeDeepeningSearch(self.problem)
        elif self.algorithm == UninformedAlgorithms.BIDIRECTIONAL_BREADTH_FIRST_SEARCH:
            init_problem = CountNodesBidirectional(self.problem)
            return BidirectionalBreathSearch(init_problem, CountNodesInverted(self.params['goal_problem'], init_problem), lambda l: 0, lambda l: 0)
        Exception("Algorithm type not supported")


class Problems(Enum):
    ROMANIA_MAP = auto()
    NPUZZLE = auto()
    N_QUEENS = auto()
    CANNIBALS_AND_MISSIONARIES = auto()


class Heuristic(Enum):
    UNATTACHED_SQUARES = auto()
    MANHATTAN = auto()
    MISPLACED_NUMBERS = auto()
    GASCHNIG = auto()
    LINERAR_CONFLICT = auto()
    STRAIGTH_LINE_DISTANCE = auto()


class AlgorithmsType(Enum):
    INFORMED = auto()
    UNINFORMED = auto()


class InformedAlgorithms(Enum):
    GREEDY_BEST_FIRST_SEARCH = auto()
    ASTAR_SEARCH = auto()
    # BEST_FIRST_GRAPH_SEARCH = auto()


class UninformedAlgorithms(Enum):
    BREADTH_FIRST_SEARCH = auto()
    DEPTH_FIRST_SEARCH = auto()
    UNIFORM_COST_SEARCH = auto()
    ITERATIVE_DEEPENING_SEARCH = auto()
    BIDIRECTIONAL_BREADTH_FIRST_SEARCH = auto()
    # DEPTH_FIRST_GRAPH_SEARCH = auto()
    # BREADTH_FIRST_GRAPH_SEARCH = auto()
    # DEPTH_LIMITED_SEARCH = auto()


