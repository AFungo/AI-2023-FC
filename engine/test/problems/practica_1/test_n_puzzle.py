import pytest

from engine.algorithms.informed.astar_searh import astar_search
from engine.algorithms.uninformed.breadth_first_graph_search import breadth_first_graph_search
from engine.problems.practica_1.n_puzzle import NPuzzle, NPuzzleState, manhattan_heuristic


@pytest.fixture
def params():
    params = {}
    params['goal_initial_state'] = NPuzzleState((1, 2, 3,
                                                 4, 5, 6,
                                                 7, 8, 0), 3)
    params['medium_initial_state'] = NPuzzleState((4, 1, 2,
                                                   7, 5, 3,
                                                   8, 0, 6), 3)
    params['advanced_initial_state'] = NPuzzleState((1, 2, 3,
                                                     4, 0, 6,
                                                     7, 8, 5), 3)
    params['n_puzzle_problem'] = NPuzzle(params['goal_initial_state'], 3)
    return params


def test_n_puzzle_breadth_first_graph_search(params):
    solution = breadth_first_graph_search(params['n_puzzle_problem']).solution()
    expected = []
    assert expected == solution


def test_n_puzzle_astar_search(params):
    solution = astar_search(params['n_puzzle_problem']).solution()
    expected = []
    assert expected == solution


def test_n_puzzle_astar_search_manhattan_heuristic(params):
    params['n_puzzle_problem'] = NPuzzle(params['advanced_initial_state'], 3)
    solution = astar_search(params['n_puzzle_problem'], manhattan_heuristic).solution()
    expected = []
    assert expected == solution
