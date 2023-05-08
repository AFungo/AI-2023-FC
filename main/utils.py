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
    df.to_csv(file_name, mode='a', header=False, index=False)


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

