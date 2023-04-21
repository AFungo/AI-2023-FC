import pytest

from engine.algorithms.uninformed.breadth_first_graph_search import breadth_first_graph_search
from engine.algorithms.uninformed.depth_first_graph_search import *
from engine.problems.practica_1.n_queeens import NQueensState, NQueensProblem, Place_A_Queen_In_Board


def test_state_is_goal():
    eight_queen = NQueensProblem(8)
    state = NQueensState(8, (7, 3, 0, 2, 5, 1, 6, 4))
    assert eight_queen.goal_test(state)


def test_state_is_not_goal():
    eight_queen = NQueensProblem(8)
    state = NQueensState(8, (1, 2, 3, 2, 5, 1, 6, 4))
    assert not eight_queen.goal_test(state)


def test_eight_queen_breadth_first_graph_search():
    eight_queen = NQueensProblem(4)
    solution = breadth_first_graph_search(eight_queen)
    assert eight_queen.goal_test(solution.state)


def test_eight():
    eight_queen = NQueensProblem(4)
    solution = depth_first_graph_search(eight_queen).solution()
    assert eight_queen.goal_test(solution.state)