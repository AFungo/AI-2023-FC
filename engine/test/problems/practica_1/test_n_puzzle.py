import os
import pytest
import datetime
from engine.utils import ComputeTimeAndMemory
from engine.problems.abstract_problem import CountNodes
from engine.algorithms.informed.best_first_graph_search import BestFirstGraphSearch
from engine.algorithms.uninformed.depth_first_search_no_cycles import DepthFirstSearchNoCycles
from engine.algorithms.uninformed.interative_deepening_search import InterativeDeepeningSearch
from engine.algorithms.informed.greedy_best_first_Search import GreedyBestFirstSearch
from engine.algorithms.informed.astar_search import AstarSearch
from engine.algorithms.uninformed.best_first_search import BestFirstSearch
from engine.algorithms.uninformed.bidirectional_breath_search import BidirectionalBreathSearch
from engine.algorithms.uninformed.breadth_first_graph_search import *
from engine.algorithms.uninformed.uniform_cost_search import UniformCostSearch
from engine.problems.practica_1.n_puzzle import NPuzzle, NPuzzleState, NPuzzleHeuristics, NPuzzleInverted

# Timeout 2m for all algorithms
pytestmark = pytest.mark.timeout(120)


@pytest.fixture
def params():
    params = {}
    params['goal_initial_state'] = NPuzzleState((1, 2, 3,
                                                 4, 5, 6,
                                                 7, 8, 0), 3)
    params['medium_initial_state'] = NPuzzleState((1, 2, 3,
                                                   4, 5, 6,
                                                   7, 0, 8), 3)

    params['advanced_initial_state'] = NPuzzleState((4, 1, 2,
                                                     7, 5, 3,
                                                     0, 8, 6), 3)

    params['5_puzzle_initial_state'] = NPuzzleState((1, 2, 3, 4, 5,
                                                     6, 7, 8, 9, 10,
                                                     11, 12, 13, 14, 15,
                                                     16, 17, 18, 0, 19,
                                                     20, 21, 22, 23, 24), 5)
    params['n_puzzle_problem'] = CountNodes(NPuzzle(params['goal_initial_state']))
    params['medium_n_puzzle'] = CountNodes(NPuzzle(params['medium_initial_state']))
    params['advanced_n_puzzle'] = CountNodes(NPuzzle(params['advanced_initial_state']))
    params['five_n_puzzle'] = CountNodes(NPuzzle(params['5_puzzle_initial_state']))
    os.remove("n_puzzle_test_suite.txt")
    params['f'] = open("n_puzzle_test_suite.txt", "w")
    # write to the file
    params['f'].write("start test suite\n")
    return params


"""Tests for Breadth-first search"""


def test_3_puzzle_easy_breadth_first_graph_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = BreadthFirstGraphSearch(params['n_puzzle_problem'])
    solution = algorithm.search().solution()
    stats.end()
    stats.print_statistics()
    print(f"\033[31mNode explored: \033[31m {params['n_puzzle_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['n_puzzle_problem'].generated_nodes}")
    assert [] == solution


def test_3_puzzle_medium_breadth_first_graph_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = BreadthFirstGraphSearch(params['medium_n_puzzle'])
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_n_puzzle'].generated_nodes}")
    assert params['medium_n_puzzle'].goal_test(solution.state)


def test_3_puzzle_advanced_breadth_first_graph_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = BreadthFirstGraphSearch(params['advanced_n_puzzle'])
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_n_puzzle'].generated_nodes}")
    assert params['advanced_n_puzzle'].goal_test(solution.state)


def test_5_puzzle_breadth_first_graph_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = BreadthFirstGraphSearch(params['five_n_puzzle'])
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['five_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['five_n_puzzle'].generated_nodes}")
    assert params['five_n_puzzle'].goal_test(solution.state)


"""Tests for Depth-first search"""


def test_3_puzzle_easy_depth_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = DepthFirstSearchNoCycles(params['n_puzzle_problem'])
    solution = algorithm.search().solution()
    stats.end()
    stats.print_statistics()
    print(f"\033[31mNode explored: \033[31m {params['n_puzzle_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['n_puzzle_problem'].generated_nodes}")
    assert [] == solution


def test_3_puzzle_medium_depth_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = DepthFirstSearchNoCycles(params['medium_n_puzzle'])
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_n_puzzle'].generated_nodes}")
    assert params['medium_n_puzzle'].goal_test(solution.state)


def test_3_puzzle_advanced_depth_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = DepthFirstSearchNoCycles(params['advanced_n_puzzle'])
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_n_puzzle'].generated_nodes}")
    assert params['advanced_n_puzzle'].goal_test(solution.state)


def test_5_puzzle_depth_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = DepthFirstSearchNoCycles(params['five_n_puzzle'])
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['five_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['five_n_puzzle'].generated_nodes}")
    assert params['five_n_puzzle'].goal_test(solution.state)


"""Tests for Uniform-cost search"""


def test_3_puzzle_easy_uniform_cost_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = UniformCostSearch(params['n_puzzle_problem'])
    solution = algorithm.search().solution()
    stats.end()
    stats.print_statistics()
    print(f"\033[31mNode explored: \033[31m {params['n_puzzle_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['n_puzzle_problem'].generated_nodes}")
    assert [] == solution


def test_3_puzzle_medium_uniform_cost_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = UniformCostSearch(params['medium_n_puzzle'])
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_n_puzzle'].generated_nodes}")
    assert params['medium_n_puzzle'].goal_test(solution.state)


def test_3_puzzle_advanced_uniform_cost_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = UniformCostSearch(params['advanced_n_puzzle'])
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_n_puzzle'].generated_nodes}")
    assert params['advanced_n_puzzle'].goal_test(solution.state)


def test_5_puzzle_uniform_cost_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = UniformCostSearch(params['five_n_puzzle'])
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['five_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['five_n_puzzle'].generated_nodes}")
    assert params['five_n_puzzle'].goal_test(solution.state)


"""Tests for Iterative deepening search"""


def test_3_puzzle_easy_iterative_deepening_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = InterativeDeepeningSearch(params['n_puzzle_problem'])
    solution = algorithm.search().solution()
    stats.end()
    stats.print_statistics()
    print(f"\033[31mNode explored: \033[31m {params['n_puzzle_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['n_puzzle_problem'].generated_nodes}")
    assert [] == solution


def test_3_puzzle_medium_iterative_deepening_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = InterativeDeepeningSearch(params['medium_n_puzzle'])
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_n_puzzle'].generated_nodes}")
    assert params['medium_n_puzzle'].goal_test(solution.state)


def test_3_puzzle_advanced_iterative_deepening_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = InterativeDeepeningSearch(params['advanced_n_puzzle'])
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_n_puzzle'].generated_nodes}")
    assert params['advanced_n_puzzle'].goal_test(solution.state)


def test_5_puzzle_iterative_deepening_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = InterativeDeepeningSearch(params['five_n_puzzle'])
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['five_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['five_n_puzzle'].generated_nodes}")
    assert params['five_n_puzzle'].goal_test(solution.state)


"""Tests for Bidirectional breadth-first search"""


def test_3_puzzle_easy_bidirectional_breadth_first_search(params):
    final_state = NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0), 3)
    final_problem = CountNodes(NPuzzleInverted(final_state))
    stats = ComputeTimeAndMemory()
    algorithm = BidirectionalBreathSearch(params['n_puzzle_problem'], final_problem, NPuzzleHeuristics().manhattan,
                                          NPuzzleHeuristics().manhattan)
    stats.start()
    solution = algorithm.search().solution()
    stats.end()
    stats.print_statistics()
    print(f"\033[31mNode explored: \033[31m {final_problem.explored_node}")
    print(f"\033[31mNode generate: \033[31m {final_problem.generated_nodes}")
    assert [] == solution


def test_3_puzzle_medium_bidirectional_breadth_first_search(params):
    stats = ComputeTimeAndMemory()
    init_problem = CountNodes(NPuzzle(params['medium_initial_state']))
    final_state = NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0), 3)
    final_problem = CountNodes(NPuzzleInverted(final_state))
    algorithm = BidirectionalBreathSearch(init_problem, final_problem, NPuzzleHeuristics().manhattan,
                                          NPuzzleHeuristics().manhattan)
    stats.start()
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {final_problem.explored_node}")
    print(f"\033[31mNode generate: \033[31m {final_problem.generated_nodes}")
    assert final_problem.goal_test(solution.state)


def test_3_puzzle_advanced_bidirectional_breadth_first_search(params):
    stats = ComputeTimeAndMemory()
    init_problem = CountNodes(NPuzzle(params['advanced_initial_state']))
    final_state = NPuzzleState((1, 2, 3, 4, 5, 6, 7, 8, 0), 3)
    final_problem = CountNodes(NPuzzleInverted(final_state))
    algorithm = BidirectionalBreathSearch(init_problem, final_problem, NPuzzleHeuristics().manhattan,
                                          NPuzzleHeuristics().manhattan)
    stats.start()
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {final_problem.explored_node}")
    print(f"\033[31mNode generate: \033[31m {final_problem.generated_nodes}")
    assert init_problem.goal_test(solution.state)


def test_5_puzzle_bidirectional_breadth_first_search(params):
    stats = ComputeTimeAndMemory()
    init_problem = CountNodes(NPuzzle(params['5_puzzle_initial_state']))
    final_state = NPuzzleState(
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 0), 5)
    final_problem = CountNodes(NPuzzleInverted(final_state))
    algorithm = BidirectionalBreathSearch(init_problem, final_problem, NPuzzleHeuristics().manhattan,
                                          NPuzzleHeuristics().manhattan)
    stats.start()
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {final_problem.explored_node}")
    print(f"\033[31mNode generate: \033[31m {final_problem.generated_nodes}")
    assert final_problem.goal_test(solution.state)


"""Tests for Greedy best-first search with heuristic manhattan"""

def test_3_puzzle_easy_greedy_best_first_search_manhattan(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['n_puzzle_problem'], NPuzzleHeuristics().manhattan)
    solution = algorithm.search().solution()
    stats.end()
    stats.print_statistics()
    print(f"\033[31mNode explored: \033[31m {params['n_puzzle_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['n_puzzle_problem'].generated_nodes}")
    assert [] == solution


def test_3_puzzle_medium_greedy_best_first_search_manhattan(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['medium_n_puzzle'], NPuzzleHeuristics().manhattan)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_n_puzzle'].generated_nodes}")
    assert params['medium_n_puzzle'].goal_test(solution.state)


def test_3_puzzle_advanced_greedy_best_first_search_manhattan(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['advanced_n_puzzle'], NPuzzleHeuristics().manhattan)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_n_puzzle'].generated_nodes}")
    assert params['advanced_n_puzzle'].goal_test(solution.state)


def test_5_puzzle_greedy_best_first_search_manhattan(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['five_n_puzzle'], NPuzzleHeuristics().manhattan)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['five_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['five_n_puzzle'].generated_nodes}")
    assert params['five_n_puzzle'].goal_test(solution.state)


"""Tests for Greedy best-first search with heuristic gaschnig"""

def test_3_puzzle_easy_greedy_best_first_search_gaschnig(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['n_puzzle_problem'], NPuzzleHeuristics().gaschnig)
    solution = algorithm.search().solution()
    stats.end()
    stats.print_statistics()
    print(f"\033[31mNode explored: \033[31m {params['n_puzzle_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['n_puzzle_problem'].generated_nodes}")
    assert [] == solution


def test_3_puzzle_medium_greedy_best_first_search_gaschnig(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['medium_n_puzzle'], NPuzzleHeuristics().gaschnig)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_n_puzzle'].generated_nodes}")
    assert params['medium_n_puzzle'].goal_test(solution.state)


def test_3_puzzle_advanced_greedy_best_first_search_gaschnig(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['advanced_n_puzzle'], NPuzzleHeuristics().gaschnig)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_n_puzzle'].generated_nodes}")
    assert params['advanced_n_puzzle'].goal_test(solution.state)


def test_5_puzzle_greedy_best_first_search_gaschnig(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['five_n_puzzle'], NPuzzleHeuristics().gaschnig)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['five_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['five_n_puzzle'].generated_nodes}")
    assert params['five_n_puzzle'].goal_test(solution.state)


"""Tests for Greedy best-first search with heuristic misplaced_numbers"""

def test_3_puzzle_easy_greedy_best_first_search_misplaced_numbers(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['n_puzzle_problem'], NPuzzleHeuristics().misplaced_numbers)
    solution = algorithm.search().solution()
    stats.end()
    stats.print_statistics()
    print(f"\033[31mNode explored: \033[31m {params['n_puzzle_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['n_puzzle_problem'].generated_nodes}")
    assert [] == solution


def test_3_puzzle_medium_greedy_best_first_search_misplaced_numbers(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['medium_n_puzzle'], NPuzzleHeuristics().misplaced_numbers)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_n_puzzle'].generated_nodes}")
    assert params['medium_n_puzzle'].goal_test(solution.state)


def test_3_puzzle_advanced_greedy_best_first_search_misplaced_numbers(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['advanced_n_puzzle'], NPuzzleHeuristics().misplaced_numbers)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_n_puzzle'].generated_nodes}")
    assert params['advanced_n_puzzle'].goal_test(solution.state)


def test_5_puzzle_greedy_best_first_search_misplaced_numbers(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['five_n_puzzle'], NPuzzleHeuristics().misplaced_numbers)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['five_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['five_n_puzzle'].generated_nodes}")
    assert params['five_n_puzzle'].goal_test(solution.state)


"""Tests for Greedy best-first search with heuristic linear_conflict"""

def test_3_puzzle_easy_greedy_best_first_search_linear_conflict(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['n_puzzle_problem'], NPuzzleHeuristics().linear_conflict)
    solution = algorithm.search().solution()
    stats.end()
    stats.print_statistics()
    print(f"\033[31mNode explored: \033[31m {params['n_puzzle_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['n_puzzle_problem'].generated_nodes}")
    assert [] == solution


def test_3_puzzle_medium_greedy_best_first_search_linear_conflict(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['medium_n_puzzle'], NPuzzleHeuristics().linear_conflict)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_n_puzzle'].generated_nodes}")
    assert params['medium_n_puzzle'].goal_test(solution.state)


def test_3_puzzle_advanced_greedy_best_first_search_linear_conflict(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['advanced_n_puzzle'], NPuzzleHeuristics().linear_conflict)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_n_puzzle'].generated_nodes}")
    assert params['advanced_n_puzzle'].goal_test(solution.state)


def test_5_puzzle_greedy_best_first_search_linear_conflict(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = GreedyBestFirstSearch(params['five_n_puzzle'], NPuzzleHeuristics().linear_conflict)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['five_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['five_n_puzzle'].generated_nodes}")
    assert params['five_n_puzzle'].goal_test(solution.state)


"""Tests for A* with heuristic manhattan"""

def test_3_puzzle_easy_astar_search_manhattan(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['n_puzzle_problem'], NPuzzleHeuristics().manhattan)
    solution = algorithm.search().solution()
    stats.end()
    stats.print_statistics()
    print(f"\033[31mNode explored: \033[31m {params['n_puzzle_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['n_puzzle_problem'].generated_nodes}")
    assert [] == solution


def test_3_puzzle_medium_astar_search_manhattan(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['medium_n_puzzle'], NPuzzleHeuristics().manhattan)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_n_puzzle'].generated_nodes}")
    assert params['medium_n_puzzle'].goal_test(solution.state)


def test_3_puzzle_advanced_astar_search_manhattan(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['advanced_n_puzzle'], NPuzzleHeuristics().manhattan)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_n_puzzle'].generated_nodes}")
    assert params['advanced_n_puzzle'].goal_test(solution.state)


def test_5_puzzle_astar_search_manhattan(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['five_n_puzzle'], NPuzzleHeuristics().manhattan)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['five_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['five_n_puzzle'].generated_nodes}")
    assert params['five_n_puzzle'].goal_test(solution.state)


"""Tests for A* with heuristic gaschnig"""

def test_3_puzzle_easy_astar_search_gaschnig(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['n_puzzle_problem'], NPuzzleHeuristics().gaschnig)
    solution = algorithm.search().solution()
    stats.end()
    stats.print_statistics()
    print(f"\033[31mNode explored: \033[31m {params['n_puzzle_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['n_puzzle_problem'].generated_nodes}")
    assert [] == solution


def test_3_puzzle_medium_astar_search_gaschnig(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['medium_n_puzzle'], NPuzzleHeuristics().gaschnig)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_n_puzzle'].generated_nodes}")
    assert params['medium_n_puzzle'].goal_test(solution.state)


def test_3_puzzle_advanced_astar_search_gaschnig(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['advanced_n_puzzle'], NPuzzleHeuristics().gaschnig)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_n_puzzle'].generated_nodes}")
    assert params['advanced_n_puzzle'].goal_test(solution.state)


def test_5_puzzle_astar_search_gaschnig(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['five_n_puzzle'], NPuzzleHeuristics().gaschnig)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['five_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['five_n_puzzle'].generated_nodes}")
    assert params['five_n_puzzle'].goal_test(solution.state)


"""Tests for A* with heuristic misplaced_numbers"""

def test_3_puzzle_easy_astar_search_misplaced_numbers(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['n_puzzle_problem'], NPuzzleHeuristics().misplaced_numbers)
    solution = algorithm.search().solution()
    stats.end()
    stats.print_statistics()
    print(f"\033[31mNode explored: \033[31m {params['n_puzzle_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['n_puzzle_problem'].generated_nodes}")
    assert [] == solution


def test_3_puzzle_medium_astar_search_misplaced_numbers(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['medium_n_puzzle'], NPuzzleHeuristics().misplaced_numbers)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_n_puzzle'].generated_nodes}")
    assert params['medium_n_puzzle'].goal_test(solution.state)


def test_3_puzzle_advanced_astar_search_misplaced_numbers(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['advanced_n_puzzle'], NPuzzleHeuristics().misplaced_numbers)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_n_puzzle'].generated_nodes}")
    assert params['advanced_n_puzzle'].goal_test(solution.state)


def test_5_puzzle_astar_search_misplaced_numbers(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['five_n_puzzle'], NPuzzleHeuristics().misplaced_numbers)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['five_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['five_n_puzzle'].generated_nodes}")
    assert params['five_n_puzzle'].goal_test(solution.state)


"""Tests for A* with heuristic linear_conflict"""

def test_3_puzzle_easy_astar_search_linear_conflict(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['n_puzzle_problem'], NPuzzleHeuristics().linear_conflict)
    solution = algorithm.search().solution()
    stats.end()
    stats.print_statistics()
    print(f"\033[31mNode explored: \033[31m {params['n_puzzle_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['n_puzzle_problem'].generated_nodes}")
    assert [] == solution


def test_3_puzzle_medium_astar_search_linear_conflict(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['medium_n_puzzle'], NPuzzleHeuristics().linear_conflict)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_n_puzzle'].generated_nodes}")
    assert params['medium_n_puzzle'].goal_test(solution.state)


def test_3_puzzle_advanced_astar_search_linear_conflict(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['advanced_n_puzzle'], NPuzzleHeuristics().linear_conflict)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_n_puzzle'].generated_nodes}")
    assert params['advanced_n_puzzle'].goal_test(solution.state)


def test_5_puzzle_astar_search_linear_conflict(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    algorithm = AstarSearch(params['five_n_puzzle'], NPuzzleHeuristics().linear_conflict)
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['five_n_puzzle'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['five_n_puzzle'].generated_nodes}")
    assert params['five_n_puzzle'].goal_test(solution.state)
