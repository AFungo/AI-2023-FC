import pytest

from engine.algorithms.uninformed.depth_first_graph_search import DepthFirstGraphSearch
from engine.algorithms.uninformed.depth_limited_search import DepthLimitedSearch
from engine.problems.abstract_problem import CountNodes
from engine.utils import ComputeTimeAndMemory
from engine.problems.practica_1.romania_map import RomaniaMap, RomaniaMapState, RomaniaMapInverted, RomaniaMapHeuristics
from engine.algorithms.uninformed.breadth_first_graph_search import BreadthFirstGraphSearch
from engine.algorithms.uninformed.depth_first_search_no_cycles import DepthFirstSearchNoCycles
from engine.algorithms.uninformed.uniform_cost_search import UniformCostSearch
from engine.algorithms.uninformed.interative_deepening_search import InterativeDeepeningSearch
from engine.algorithms.uninformed.bidirectional_breath_search import BidirectionalBreathSearch
from engine.algorithms.informed.greedy_best_first_Search import GreedyBestFirstSearch
from engine.algorithms.informed.astar_search import AstarSearch

# Timeout 2m for all algorithms
pytestmark = pytest.mark.timeout(120)


@pytest.fixture
def params():
    params = {}

    # Initial states
    params["easy_initial_state"] = RomaniaMapState('Arad')
    params["medium_initial_state"] = RomaniaMapState('Vaslui')
    params["advanced_initial_state"] = RomaniaMapState('Oradea')

    # Goal states
    params["easy_goal_state"] = RomaniaMapState('Fagaras')
    params["medium_goal_state"] = RomaniaMapState('Rimnicu')
    params["advanced_goal_state"] = RomaniaMapState('Eforie')
    params["other_goal_state"] = RomaniaMapState('Bucharest')

    # Romania problems
    params["easy_romania_problem"] = CountNodes(RomaniaMap(params["easy_initial_state"], params["easy_goal_state"]))
    params["medium_romania_problem"] = CountNodes(
        RomaniaMap(params["medium_initial_state"], params["medium_goal_state"]))
    params["advanced_romania_problem"] = CountNodes(
        RomaniaMap(params["advanced_initial_state"], params["advanced_goal_state"]))

    params["romania_problem"] = RomaniaMap(params["easy_initial_state"], params["other_goal_state"])

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
    expected = ['(Arad, Timisoara)',
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


def test_bidirectional_breath_search(params):
    expected = ['(Arad, Sibiu)', '(Sibiu, Fagaras)', '(Fagaras, Bucharest)']
    final_problem = RomaniaMapInverted(params["other_goal_state"])
    algorithm = BidirectionalBreathSearch(params["romania_problem"], final_problem,
                                          lambda l: l.path_cost, lambda l: l.path_cost
                                          )
    solution = algorithm.search()
    solution_path = list(map(lambda l: l.__str__(), solution.path()))
    solution_actions = list(map(lambda l: l.__str__(), solution.solution()))
    assert solution_actions == expected

    """ Tests with breadth_first_graph_search"""


def test_easy_romania_breadth_first_graph_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = BreadthFirstGraphSearch(params["easy_romania_problem"]).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["easy_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['easy_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['easy_romania_problem'].generated_nodes}")
    assert solution.state == params["easy_goal_state"]


def test_medium_romania_breadth_first_graph_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = BreadthFirstGraphSearch(params["medium_romania_problem"]).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["medium_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_romania_problem'].generated_nodes}")
    assert solution.state == params["medium_goal_state"]


def test_advanced_romania_breadth_first_graph_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = BreadthFirstGraphSearch(params["advanced_romania_problem"]).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["advanced_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_romania_problem'].generated_nodes}")
    assert solution.state == params["advanced_goal_state"]

    """ Tests with depth_first_search"""


def test_easy_romania_depth_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = DepthFirstSearchNoCycles(params["easy_romania_problem"]).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["easy_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['easy_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['easy_romania_problem'].generated_nodes}")
    assert solution.state == params["easy_goal_state"]


def test_medium_romania_depth_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = DepthFirstSearchNoCycles(params["medium_romania_problem"]).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["medium_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_romania_problem'].generated_nodes}")
    assert solution.state == params["medium_goal_state"]


def test_advanced_romania_depth_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = DepthFirstSearchNoCycles(params["advanced_romania_problem"]).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["advanced_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_romania_problem'].generated_nodes}")
    assert solution.state == params["advanced_goal_state"]

    """ Tests with Uniform-cost search"""


def test_easy_romania_uniform_cost_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = UniformCostSearch(params["easy_romania_problem"]).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["easy_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['easy_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['easy_romania_problem'].generated_nodes}")
    assert solution.state == params["easy_goal_state"]


def test_medium_romania_uniform_cost_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = UniformCostSearch(params["medium_romania_problem"]).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["medium_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_romania_problem'].generated_nodes}")
    assert solution.state == params["medium_goal_state"]


def test_advanced_romania_uniform_cost_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = UniformCostSearch(params["advanced_romania_problem"]).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["advanced_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_romania_problem'].generated_nodes}")
    assert solution.state == params["advanced_goal_state"]

    """ Tests with Iterative deepening search"""


def test_easy_romania_iterative_deepening_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = InterativeDeepeningSearch(params["easy_romania_problem"]).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["easy_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['easy_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['easy_romania_problem'].generated_nodes}")
    assert solution.state == params["easy_goal_state"]


def test_medium_romania_iterative_deepening_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = InterativeDeepeningSearch(params["medium_romania_problem"]).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["medium_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_romania_problem'].generated_nodes}")
    assert solution.state == params["medium_goal_state"]


def test_advanced_romania_iterative_deepening_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = InterativeDeepeningSearch(params["advanced_romania_problem"]).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["advanced_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_romania_problem'].generated_nodes}")
    assert solution.state == params["advanced_goal_state"]

    """ Tests with Greedy best-first search"""


def test_easy_romania_greedy_best_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = GreedyBestFirstSearch(params["easy_romania_problem"], lambda l: l.path_cost).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["easy_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['easy_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['easy_romania_problem'].generated_nodes}")
    assert solution.state == params["easy_goal_state"]


def test_medium_romania_greedy_best_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = GreedyBestFirstSearch(params["medium_romania_problem"], lambda l: l.path_cost).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["medium_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_romania_problem'].generated_nodes}")
    assert solution.state == params["medium_goal_state"]


def test_advanced_romania_greedy_best_first_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = GreedyBestFirstSearch(params["advanced_romania_problem"], lambda l: l.path_cost).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["advanced_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_romania_problem'].generated_nodes}")
    assert solution.state == params["advanced_goal_state"]

    """ Tests with A*"""


def test_easy_romania_astar_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = AstarSearch(params["easy_romania_problem"], lambda l: l.path_cost).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["easy_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['easy_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['easy_romania_problem'].generated_nodes}")
    assert solution.state == params["easy_goal_state"]


def test_medium_romania_astar_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    h = RomaniaMapHeuristics('Rimnicu').straigth_line_distance
    solution = AstarSearch(params["medium_romania_problem"], lambda n: h(n)).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["medium_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['medium_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['medium_romania_problem'].generated_nodes}")
    assert solution.state == params["medium_goal_state"]


def test_advanced_romania_astar_search(params):
    stats = ComputeTimeAndMemory()
    stats.start()
    solution = AstarSearch(params["advanced_romania_problem"], lambda l: l.path_cost).search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(params["advanced_initial_state"].city))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    print(f"\033[31mNode explored: \033[31m {params['advanced_romania_problem'].explored_node}")
    print(f"\033[31mNode generate: \033[31m {params['advanced_romania_problem'].generated_nodes}")
    assert solution.state == params["advanced_goal_state"]

    """Tests for Bidirectional breadth-first search"""
    # Problema: el problema es que como la bidirectinal toma el romania map y el inverted
    # al decorarlos con el countNodes esa clase no tiene la city :(

def test_easy_bidirectional_breath_search(params):

    stats = ComputeTimeAndMemory()
    initial_problem = RomaniaMap(params["easy_initial_state"], params["easy_goal_state"])
    final_problem = RomaniaMapInverted(params["easy_goal_state"])

    algorithm = BidirectionalBreathSearch(initial_problem, final_problem, lambda l: l.path_cost, lambda l: l.path_cost)
    stats.start()
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(initial_problem.initial_state()))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    # print(f"\033[31mNode explored: \033[31m {params['easy_romania_problem'].explored_node}")
    # print(f"\033[31mNode generate: \033[31m {params['easy_romania_problem'].generated_nodes}")
    assert solution.state == params["easy_goal_state"]


def test_medium_bidirectional_breath_search(params):

    stats = ComputeTimeAndMemory()
    initial_problem = RomaniaMap(params["medium_initial_state"], params["medium_goal_state"])
    final_problem = RomaniaMapInverted(params["medium_goal_state"])

    algorithm = BidirectionalBreathSearch(initial_problem, final_problem, lambda l: l.path_cost, lambda l: l.path_cost)
    stats.start()
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(initial_problem.initial_state()))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    # print(f"\033[31mNode explored: \033[31m {params['medium_romania_problem'].explored_node}")
    # print(f"\033[31mNode generate: \033[31m {params['medium_romania_problem'].generated_nodes}")
    assert solution.state == params["medium_goal_state"]


def test_advanced_bidirectional_breath_search(params):

    stats = ComputeTimeAndMemory()
    initial_problem = RomaniaMap(params["advanced_initial_state"], params["advanced_goal_state"])
    final_problem = RomaniaMapInverted(params["advanced_goal_state"])

    algorithm = BidirectionalBreathSearch(initial_problem, final_problem, lambda l: l.path_cost, lambda l: l.path_cost)
    stats.start()
    solution = algorithm.search()
    stats.end()
    stats.print_statistics()
    print("\033[32mDepature city: \033[32m" + str(initial_problem.initial_state()))
    print("\033[32mArrival city: \033[32m" + str(solution.state))
    print("\033[35mPath Cost: \033[35m" + str(solution.path_cost))
    print("\033[36mDepth: \033[36m" + str(solution.depth))
    # print(f"\033[31mNode explored: \033[31m {params['advanced_romania_problem'].explored_node}")
    # print(f"\033[31mNode generate: \033[31m {params['advanced_romania_problem'].generated_nodes}")
    assert solution.state == params["advanced_goal_state"]