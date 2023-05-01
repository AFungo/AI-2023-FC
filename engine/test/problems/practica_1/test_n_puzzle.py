import os

import pytest

from engine.algorithms.informed.astar_search import AstarSearch
from engine.algorithms.informed.best_first_graph_search import BestFirstGraphSearch
from engine.algorithms.uninformed.best_first_search import BestFirstSearch
from engine.algorithms.uninformed.breadth_first_graph_search import *
from engine.algorithms.uninformed.uniform_cost_search import UniformCostSearch
from engine.problems.practica_1.n_puzzle import NPuzzle, NPuzzleState, NPuzzleHeuristics
import datetime


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
    params['n_puzzle_problem'] = NPuzzle(params['goal_initial_state'], 3)
    os.remove("n_puzzle_test_suite.txt")
    params['f'] = open("n_puzzle_test_suite.txt", "w")
    # write to the file
    params['f'].write("start test suite\n")
    return params


def test_n_puzzle_breadth_first_graph_search(params):
    algorithm = BreadthFirstGraphSearch(params['n_puzzle_problem'])
    solution = algorithm.search().solution()
    expected = []
    assert expected == solution


def test_3_puzzle_astar_search_default_heuristic_winner_state(params):
    algorithm = AstarSearch(params['n_puzzle_problem'], NPuzzleHeuristics().misplaced_numbers)
    solution = algorithm.search().solution()
    expected = []
    assert expected == solution


def test_3_puzzle_astar_search_default_heuristic_medium_state(params):
    problem = NPuzzle(params['medium_initial_state'], 3)
    algorithm = AstarSearch(problem, NPuzzleHeuristics().misplaced_numbers)
    solution = algorithm.search().solution()
    expected = []
    assert expected == solution


def test_3_puzzle_astar_search_default_heuristic_advanced_state(params):
    problem = NPuzzle(params['advanced_initial_state'], 3)
    algorithm = AstarSearch(problem, NPuzzleHeuristics().misplaced_numbers)
    solution = algorithm.search().solution()
    expected = []
    assert expected == solution


def test_3_puzzle_astar_search_manhattan_heuristic_medium_initial_state(params):
    problem = NPuzzle(params['medium_initial_state'], 3)
    algorithm = AstarSearch(problem, NPuzzleHeuristics().manhattan)
    solution = algorithm.search().solution()
    expected = []
    assert expected == solution


def test_3_puzzle_best_first_search_manhattan_heuristic_medium_initial_state(params):
    problem = NPuzzle(params['medium_initial_state'], 3)
    bfs = BestFirstSearch(problem, NPuzzleHeuristics().manhattan)
    bfs_book = BestFirstGraphSearch(problem, NPuzzleHeuristics().manhattan)
    bfs_solution = bfs.search().solution()
    bfs_book_solution = bfs_book.search().solution()
    expected = []
    assert bfs_solution == bfs_book_solution


def test_3_puzzle_uniform_cost_search_manhattan_heuristic_medium_initial_state(params):
    problem = NPuzzle(params['medium_initial_state'], 3)
    bfs = UniformCostSearch(problem)
    bfs_book = BestFirstGraphSearch(problem, NPuzzleHeuristics().manhattan)
    bfs_solution = bfs.search().solution()
    bfs_book_solution = bfs_book.search().solution()
    expected = []
    assert bfs_solution == []  # bfs_book_solution


def test_3_puzzle_astar_search_manhattan_heuristic_advanced_initial_state(params):
    params['f'].write("3 - puzzle" + datetime.datetime.now().__str__() + " - ")
    problem = NPuzzle(params['advanced_initial_state'], 3)
    algorithm = AstarSearch(problem, NPuzzleHeuristics().manhattan)
    solution = algorithm.search().solution()
    expected = []
    params['f'].write(datetime.datetime.now().__str__() + "\n")
    assert expected == solution


def test_3_puzzle_astar_search_linear_conflict_advanced_initial_state(params):
    # params['f'].write("3 - puzzle" + datetime.datetime.now().__str__() + " - ")
    problem = NPuzzle(params['advanced_initial_state'], 3)
    algorithm = AstarSearch(problem, NPuzzleHeuristics().linear_conflict)
    solution = algorithm.search().solution()
    expected = []
    # params['f'].write(datetime.datetime.now().__str__() + "\n")
    assert expected == solution

def test_3_puzzle_astar_search_gasching_advanced_initial_state(params):
    # params['f'].write("3 - puzzle" + datetime.datetime.now().__str__() + " - ")
    problem = NPuzzle(params['advanced_initial_state'], 3)
    algorithm = AstarSearch(problem, NPuzzleHeuristics().gaschnig)
    solution = algorithm.search().solution()
    expected = []
    # params['f'].write(datetime.datetime.now().__str__() + "\n")
    assert expected == solution

def test_5_puzzle_astar_search_manhattan_heuristic(params):
    params['f'].write("5 - puzzle" + datetime.datetime.now().__str__() + " - ")
    problem = NPuzzle(params['5_puzzle_initial_state'], 3)
    algorithm = AstarSearch(problem, NPuzzleHeuristics().manhattan)
    solution = algorithm.search().solution()
    expected = []
    params['f'].write(datetime.datetime.now().__str__() + "\n")
    assert expected == solution
