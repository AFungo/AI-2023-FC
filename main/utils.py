import pandas as pd

from engine.engine import UninformedAlgorithms, InformedAlgorithms, Heuristic, Problems


def algorithm_parser(name):
    try:
        algorithm = UninformedAlgorithms.__members__[name]
    except KeyError:
        try:
            algorithm = InformedAlgorithms.__members__[name]
        except KeyError:
            raise Exception("Algorithm not supported")
    return algorithm


def export_data(solution, file_name):
    df = pd.DataFrame(solution, index=[0])
    df.to_csv(file_name, mode='a', header=True, index=False)


def n_puzzle_check_solvability(state):
    """ Checks if the given state is solvable """
    inversion = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                inversion += 1

    return inversion % 2 == 0


def n_puzzle_generate_goal_state(size):
    array = []
    for i in range(size - 1):
        array.append(i + 1)
    array.append(0)
    return array


def algorithm_name(name):
    if name == "ASTAR_SEARCH":
        return "AstarSearch"
    elif name == "BREADTH_FIRST_SEARCH":
        return "BreadthFirstGraphSearch"
    elif name == "DEPTH_FIRST_SEARCH":
        return "DepthFirstSearch"
    elif name == "GREEDY_BEST_FIRST_SEARCH":
        return "GreedyBestFirstSearch"
    elif name == "ITERATIVE_DEEPENING_SEARCH":
        return "InterativeDeepeningSearch"
    elif name == "UNIFORM_COST_SEARCH":
        return "UniformCostSearch"
    Exception("Algorithm not supported")


def heuristic_parser(heuristic):
    try:
        return Heuristic.__members__[heuristic]
    except KeyError:
        return None


def get_heuristic_name(heuristic):
    if heuristic is None:
        return None
    return heuristic.name


def parse_data_to_dictionary(problem, algorithm, heuristic, initial_state, goal_state=None, depth=None,
                             explored_nodes=None, generated_nodes=None, memory=None, run_time=None,
                             path_cost=None, path=None, solution=None):

    solution = {"problem": problem.name,
                "algorithm": algorithm.name,
                "heuristic": get_heuristic_name(heuristic),
                "initial_state": initial_state.__str__(),
                "goal_state": str(goal_state),
                "depth": none_data_to_string(depth),
                "explored_nodes": none_data_to_string(explored_nodes),
                "generated_nodes": none_data_to_string(generated_nodes),
                "Memory": none_data_to_string(memory),
                "run_time": none_data_to_string(run_time),
                "path_cost": none_data_to_string(path_cost),
                "path": path_to_string(path),
                "solution": solution_to_string(solution)
                }
    return solution

def none_data_to_string(value):
    if value is not None:
        return value
    return " "


def solution_to_string(solution):
    if solution is not None:
        return str(list(map(lambda l: l.__str__(), solution)))
    return " "


def path_to_string(path):
    if path is not None:
        return str(list(map(lambda l: l.state.__str__(), path)))
    return " "