import pytest
from engine.algorithms.uninformed.breadth_first_graph_search import BreadthFirstGraphSearch
from engine.algorithms.uninformed.depth_first_search_no_cycles import DepthFirstSearchNoCycles
from engine.algorithms.uninformed.uniform_cost_search import UniformCostSearch
from engine.algorithms.uninformed.interative_deepening_search import InterativeDeepeningSearch
from engine.algorithms.informed.greedy_best_first_Search import GreedyBestFirstSearch
from engine.algorithms.informed.astar_search import AstarSearch
from engine.problems.practica_1.n_queeens import NQueensState, NQueensProblem, NQueensHeuristics
from engine.problems.abstract_problem import CountNodes
from engine.utils import ComputeTimeAndMemory


# Timeout 2m for all algorithms
pytestmark = pytest.mark.timeout(120)

@pytest.fixture
def params():
    params = {'four_queens': CountNodes(NQueensProblem(4)), 'six_queens': CountNodes(NQueensProblem(6)),
              'eight_queens': CountNodes(NQueensProblem(8)), 'nine_queens': CountNodes(NQueensProblem(9))}
    return params


def test_state_is_goal(params):
    state = NQueensState(8, (7, 3, 0, 2, 5, 1, 6, 4))
    assert params['eight_queens'].goal_test(state)


def test_state_is_not_goal(params):
    state = NQueensState(8, (1, 2, 3, 2, 5, 1, 6, 4))
    assert not params['eight_queens'].goal_test(state)


""" Tests with breadth_first_graph_search"""


def test_four_queen_breadth_first_graph_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = BreadthFirstGraphSearch(params['four_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['four_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['four_queens'].generated_nodes}")
    assert params['four_queens'].goal_test(solution.state)


def test_six_queen_breadth_first_graph_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = BreadthFirstGraphSearch(params['six_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['six_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['six_queens'].generated_nodes}")
    assert params['six_queens'].goal_test(solution.state)


def test_eight_queen_breadth_first_graph_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = BreadthFirstGraphSearch(params['eight_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['eight_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['eight_queens'].generated_nodes}")
    assert params['eight_queens'].goal_test(solution.state)


def test_nine_queen_breadth_first_graph_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = BreadthFirstGraphSearch(params['nine_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['nine_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['nine_queens'].generated_nodes}")
    assert params['nine_queens'].goal_test(solution.state)


""" Tests with depth_first_search"""


def test_four_queen_depth_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = DepthFirstSearchNoCycles(params['four_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['four_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['four_queens'].generated_nodes}")
    assert params['four_queens'].goal_test(solution.state)


def test_six_queen_depth_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = DepthFirstSearchNoCycles(params['six_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['six_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['six_queens'].generated_nodes}")
    assert params['six_queens'].goal_test(solution.state)


def test_eight_queen_depth_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = DepthFirstSearchNoCycles(params['eight_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['eight_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['eight_queens'].generated_nodes}")
    assert params['eight_queens'].goal_test(solution.state)


def test_nine_queen_depth_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = DepthFirstSearchNoCycles(params['nine_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['nine_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['nine_queens'].generated_nodes}")
    assert params['nine_queens'].goal_test(solution.state)


""" Tests with Uniform-cost search"""


def test_four_queen_uniform_cost_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = UniformCostSearch(params['four_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['four_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['four_queens'].generated_nodes}")
    assert params['four_queens'].goal_test(solution.state)


def test_six_queen_uniform_cost_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = UniformCostSearch(params['six_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['six_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['six_queens'].generated_nodes}")
    assert params['six_queens'].goal_test(solution.state)


def test_eight_queen_uniform_cost_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = UniformCostSearch(params['eight_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['eight_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['eight_queens'].generated_nodes}")
    assert params['eight_queens'].goal_test(solution.state)


def test_nine_queen_uniform_cost_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = UniformCostSearch(params['nine_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['nine_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['nine_queens'].generated_nodes}")
    assert params['nine_queens'].goal_test(solution.state)


""" Tests with Iterative deepening search"""


def test_four_queen_iterative_deepening_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = InterativeDeepeningSearch(params['four_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['four_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['four_queens'].generated_nodes}")
    assert params['four_queens'].goal_test(solution.state)


def test_six_queen_iterative_deepening_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = InterativeDeepeningSearch(params['six_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['six_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['six_queens'].generated_nodes}")
    assert params['six_queens'].goal_test(solution.state)


def test_eight_queen_iterative_deepening_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = InterativeDeepeningSearch(params['eight_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['eight_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['eight_queens'].generated_nodes}")
    assert params['eight_queens'].goal_test(solution.state)


def test_nine_queen_iterative_deepening_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = InterativeDeepeningSearch(params['nine_queens']).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['nine_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['nine_queens'].generated_nodes}")
    assert params['nine_queens'].goal_test(solution.state)


""" Tests with Greedy best-first search"""


def test_four_queen_greedy_best_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = GreedyBestFirstSearch(params['four_queens'], NQueensHeuristics().unattacked_squares).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['four_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['four_queens'].generated_nodes}")
    assert params['four_queens'].goal_test(solution.state)


def test_six_queen_greedy_best_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = GreedyBestFirstSearch(params['six_queens'], NQueensHeuristics().unattacked_squares).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['six_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['six_queens'].generated_nodes}")
    assert params['six_queens'].goal_test(solution.state)


def test_eight_queen_greedy_best_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = GreedyBestFirstSearch(params['eight_queens'], NQueensHeuristics().unattacked_squares).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['eight_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['eight_queens'].generated_nodes}")
    assert params['eight_queens'].goal_test(solution.state)


def test_nine_queen_greedy_best_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = GreedyBestFirstSearch(params['nine_queens'], NQueensHeuristics().unattacked_squares).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['nine_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['nine_queens'].generated_nodes}")
    assert params['nine_queens'].goal_test(solution.state)


""" Tests with A*"""


def test_four_queen_astar_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = AstarSearch(params['four_queens'], NQueensHeuristics().unattacked_squares).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['four_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['four_queens'].generated_nodes}")
    assert params['four_queens'].goal_test(solution.state)


def test_six_queen_astar_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = AstarSearch(params['six_queens'], NQueensHeuristics().unattacked_squares).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['six_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['six_queens'].generated_nodes}")
    assert params['six_queens'].goal_test(solution.state)


def test_eight_queen_astar_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = AstarSearch(params['eight_queens'], NQueensHeuristics().unattacked_squares).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['eight_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['eight_queens'].generated_nodes}")
    assert params['eight_queens'].goal_test(solution.state)


def test_nine_queen_astar_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = AstarSearch(params['nine_queens'], NQueensHeuristics().unattacked_squares).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mWin state: \033[32m" + str(solution.state.board))
    print(f"\033[31mNode explored: \033[31m {params['nine_queens'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['nine_queens'].generated_nodes}")
    assert params['nine_queens'].goal_test(solution.state)
