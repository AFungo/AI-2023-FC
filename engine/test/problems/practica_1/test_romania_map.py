from engine.algorithms.uninformed.breadth_first_graph_search import breadth_first_graph_search
from engine.algorithms.uninformed.depth_first_graph_search import depth_first_graph_search
from engine.problems.practica_1.romania_map import RomaniaMap, RomaniaMapState
from engine.utils import UndirectedGraph

initial_state = RomaniaMapState('Arad')
goal_state = RomaniaMapState('Bucharest')
romania_problem = RomaniaMap(initial_state, goal_state)


def test_depth_first_search():
    expected = ['Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova', 'Pitesti', 'Bucharest']
    solution = list(map(
        lambda l: l.__str__(), depth_first_graph_search(romania_problem).solution()))
    assert solution == expected


def test_find_min_edge():
    assert romania_problem.find_min_edge() == 70


def test_breadth_first_tree_search():
    expected = ['Sibiu', 'Fagaras', 'Bucharest']
    solution = list(map(
        lambda l: l.__str__(), breadth_first_graph_search(
            romania_problem).solution()))
    assert expected == solution
