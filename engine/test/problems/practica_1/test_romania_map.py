from engine.algorithms.uninformed.bidirectional_breath_search import BidirectionalBreathSearch
from engine.algorithms.uninformed.breadth_first_graph_search import BreadthFirstGraphSearch
from engine.algorithms.uninformed.depth_first_graph_search import DepthFirstGraphSearch
from engine.algorithms.uninformed.depth_first_search_no_cycles import DepthFirstSearchNoCycles
from engine.algorithms.uninformed.depth_limited_search import DepthLimitedSearch
from engine.algorithms.uninformed.interative_deepening_search import InterativeDeepeningSearch
from engine.problems.practica_1.romania_map import RomaniaMap, RomaniaMapState, RomaniaMapInverted
from engine.utils import UndirectedGraph
import pytest


@pytest.fixture
def params():
    params = {}
    params["initial_state"] = RomaniaMapState('Arad')
    params["goal_state"] = RomaniaMapState('Bucharest')
    params["romania_problem"] = RomaniaMap(params["initial_state"], params["goal_state"])
    return params


def test_find_min_edge(params):
    assert params["romania_problem"].find_min_edge() == 70


def test_depth_first_search(params):
    expected = ['(Arad, Timisoara)',
                '(Timisoara, Lugoj)',
                '(Lugoj, Mehadia)',
                '(Mehadia, Drobeta)',
                '(Drobeta, Craiova)',
                '(Craiova, Pitesti)',
                '(Pitesti, Bucharest)'
                ]
    algorithm = DepthFirstGraphSearch(params["romania_problem"])
    solution = list(map(
        lambda l: l.__str__(), algorithm.search().solution()))
    assert solution == expected


def test_breadth_first_tree_search(params):
    expected = ['(Arad, Sibiu)', '(Sibiu, Fagaras)', '(Fagaras, Bucharest)']
    algorithm = BreadthFirstGraphSearch(params["romania_problem"])
    solution = list(map(lambda l: l.__str__(), algorithm.search().solution()))
    assert expected == solution


def test_depth_frist_search_no_cycles(params):
    expected =['(Arad, Timisoara)',
                '(Timisoara, Lugoj)',
                '(Lugoj, Mehadia)',
                '(Mehadia, Drobeta)',
                '(Drobeta, Craiova)',
                '(Craiova, Pitesti)',
                '(Pitesti, Bucharest)'
               ]
    algorithm = DepthFirstSearchNoCycles(params["romania_problem"])
    solution = algorithm.search().solution()
    solution = list(map(lambda l: l.__str__(), solution))
    assert expected == solution


def test_depth_limited_search(params):
    expected = ['(Arad, Timisoara)',
                 '(Timisoara, Lugoj)',
                 '(Lugoj, Mehadia)',
                 '(Mehadia, Drobeta)',
                 '(Drobeta, Craiova)',
                 '(Craiova, Pitesti)',
                 '(Pitesti, Bucharest)'
                ]
    algorithm = DepthLimitedSearch(params["romania_problem"], 19)
    solution = list(map(lambda l: l.__str__(), algorithm.search().solution()))
    assert expected == solution


# def test_iterative_deepening_search(params):
#     expected = ['(Arad, Sibiu)', '(Sibiu, Fagaras)', '(Fagaras, Bucharest)']
#     algorithm = InterativeDeepeningSearch(params["romania_problem"])
#     solution = list(map(lambda l: l.__str__(), algorithm.search().solution()))
#     assert expected == solution


def test_bidirectional_breath_search(params):
    expected = ['(Arad, Sibiu)', '(Sibiu, Fagaras)', '(Fagaras, Bucharest)']
    final_problem = RomaniaMapInverted(params["goal_state"])
    algorithm = BidirectionalBreathSearch(params["romania_problem"], final_problem,
                                          lambda l: l.path_cost, lambda l: l.path_cost
                                          )
    solution = algorithm.search()
    solution_path = list(map(lambda l: l.__str__(), solution.path()))
    solution_actions = list(map(lambda l: l.__str__(), solution.solution()))
    assert solution_actions == expected
