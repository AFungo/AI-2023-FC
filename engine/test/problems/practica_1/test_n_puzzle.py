import os

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
    params['medium_initial_state'] = NPuzzleState((4, 2, 0,
                                                   7, 1, 3,
                                                   8, 5, 6), 3)
    params['advanced_initial_state'] = NPuzzleState((7, 2, 4,
                                                     5, 0, 6,
                                                     8, 3, 1), 3)
    params['5_puzzle_initial_state'] = NPuzzleState((1, 2, 3, 4, 5,
                                                      6, 7, 8, 9, 10,
                                                      11, 12, 13, 14, 15,
                                                      16, 17, 18, 0, 19,
                                                      20, 21, 22, 23, 24), 5)
    params['n_puzzle_problem'] = NPuzzle(params['goal_initial_state'], 3)
    os.remove("n_puzzle_test_suite.txt")
    params['f'] = open("n_puzzle_test_suite.txt", "w")
    # write to the file
    params['f'].write("start test suite\n")
    return params


def test_n_puzzle_breadth_first_graph_search(params):
    solution = breadth_first_graph_search(params['n_puzzle_problem']).solution()
    expected = []
    assert expected == solution


def test_3_puzzle_astar_search_default_heuristic_winner_state(params):
    solution = astar_search(params['n_puzzle_problem']).solution()
    expected = []
    assert expected == solution


def test_3_puzzle_astar_search_default_heuristic_medium_state(params):
    params['n_puzzle_problem'] = NPuzzle(params['medium_initial_state'], 3)
    solution = astar_search(params['n_puzzle_problem']).solution()
    expected = []
    assert expected == solution


def test_3_puzzle_astar_search_default_heuristic_advanced_state(params):
    params['n_puzzle_problem'] = NPuzzle(params['advanced_initial_state'], 3)
    solution = astar_search(params['n_puzzle_problem']).solution()
    expected = []
    assert expected == solution


def test_3_puzzle_astar_search_manhattan_heuristic_medium_initial_state(params):
    params['n_puzzle_problem'] = NPuzzle(params['medium_initial_state'], 3)
    solution = astar_search(params['n_puzzle_problem'], manhattan_heuristic).solution()
    expected = []
    assert expected == solution


import datetime


def test_3_puzzle_astar_search_manhattan_heuristic_advanced_initial_state(params):
    params['f'].write("3 - puzzle" + datetime.datetime.now().__str__() + " - ")
    params['n_puzzle_problem'] = NPuzzle(params['advanced_initial_state'], 3)
    solution = astar_search(params['n_puzzle_problem'], manhattan_heuristic).solution()
    expected = []
    params['f'].write(datetime.datetime.now().__str__() + "\n")
    assert expected == solution


def test_5_puzzle_astar_search_manhattan_heuristic(params):
    params['f'].write("5 - puzzle" + datetime.datetime.now().__str__() + " - ")
    params['n_puzzle_problem'] = NPuzzle(params['5_puzzle_initial_state'], 5)
    solution = astar_search(params['n_puzzle_problem'], manhattan_heuristic).solution()
    expected = []
    params['f'].write(datetime.datetime.now().__str__() + "\n")
    assert expected == solution
