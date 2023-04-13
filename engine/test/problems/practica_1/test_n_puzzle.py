import pytest

from engine.algorithms.uninformed.breadth_first_graph_search import breadth_first_graph_search
from engine.problems.practica_1.n_puzzle import NPuzzle, NPuzzleState


@pytest.fixture
def params():
    params = {}
    params['initial_state'] = NPuzzleState((1, 2, 3,
                                            0, 5, 4,
                                            7, 8, 6))
    params['n_puzzle_problem'] = NPuzzle(params['initial_state'], 3)
    return params


def test_n_puzzle_breadth_first_graph_search(params):
    solution = breadth_first_graph_search(params['n_puzzle_problem']).solution()
    expected = []
    assert expected == solution
