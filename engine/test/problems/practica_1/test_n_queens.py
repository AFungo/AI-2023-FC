import pytest

from engine.algorithms.uninformed.breadth_first_graph_search import BreadthFirstGraphSearch
from engine.algorithms.uninformed.depth_first_search import DepthFirstSearch
from engine.algorithms.uninformed.depth_first_search_no_cycles import DepthFirstSearchNoCycles
from engine.problems.practica_1.n_queeens import NQueensState, NQueensProblem, Place_A_Queen_In_Board


def test_state_is_goal():
    eight_queen = NQueensProblem(8)
    state = NQueensState(8, (7, 3, 0, 2, 5, 1, 6, 4))
    assert eight_queen.goal_test(state)


def test_state_is_not_goal():
    eight_queen = NQueensProblem(8)
    state = NQueensState(8, (1, 2, 3, 2, 5, 1, 6, 4))
    assert not eight_queen.goal_test(state)


def test_four_queen_breadth_first_graph_search():
    four_queen = NQueensProblem(4)
    solution = BreadthFirstGraphSearch(four_queen).search()
    print("\n\033[32mWin state: \033[32m" + str(solution.state.board))
    assert four_queen.goal_test(solution.state)


def test_five_queen_breadth_first_graph_search():
    five_queen = NQueensProblem(5)
    solution = BreadthFirstGraphSearch(five_queen).search()
    print("\n\033[32mWin state: \033[32m" + str(solution.state.board))
    assert five_queen.goal_test(solution.state)


def test_six_queen_breadth_first_graph_search():
    six_queen = NQueensProblem(6)
    solution = BreadthFirstGraphSearch(six_queen).search()
    print("\n\033[32mWin state: \033[32m" + str(solution.state.board))
    assert six_queen.goal_test(solution.state)


def test_seven_queen_breadth_first_graph_search():
    seven_queen = NQueensProblem(7)
    solution = BreadthFirstGraphSearch(seven_queen).search()
    print("\n\033[32mWin state: \033[32m" + str(solution.state.board))
    assert seven_queen.goal_test(solution.state)


def test_eight_queen_breadth_first_graph_search():
    eight_queen = NQueensProblem(8)
    solution = BreadthFirstGraphSearch(eight_queen).search()
    print("\n\033[32mWin state: \033[32m" + str(solution.state.board))
    assert eight_queen.goal_test(solution.state)

def test_four_queen_depth_first_search():
    four_queen = NQueensProblem(4)
    solution = DepthFirstSearchNoCycles(four_queen).search()
    print("\n\033[32mWin state: \033[32m" + str(solution.state.board))
    assert four_queen.goal_test(solution.state)