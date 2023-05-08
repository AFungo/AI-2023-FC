import ast
import re
import pandas as pd
import itertools
import random
import sys

from numpy.core._multiarray_umath import sqrt
from engine.engine import *
from engine.problems.practica_1.n_puzzle import NPuzzleState, NPuzzleInverted
from main.utils import export_data, algorithm_parser, n_puzzle_check_solvability, n_puzzle_generate_goal_state, \
    heuristic_parser
from engine.engine import UninformedAlgorithms, InformedAlgorithms, Problems


def main(row):
    data = parse_n_puzzle(row)
    problem_params = {"initial_state": data["init_state"]}
    algorithm_params = {"goal_problem": NPuzzleInverted(data["goal_state"])}
    engine = Engine(data["problem"], data["algorithm"], problem_params, data["heuristic"], algorithm_params=algorithm_params)
    solution = engine.solve()
    export_data(solution, data["output_file"])


def add_row(problem, algorithm, algorithm_params, heuristic, initial_state, n, goal_state, output_file, csv_file):
    data = {'problem': problem,
            'algorithm': algorithm,
            'algorithm_params': algorithm_params,
            'heuristic': heuristic,
            'initial_state': initial_state,
            'n': n,
            'goal_state': goal_state,
            'output_file': output_file
            }
    df = pd.DataFrame(data, index=[0])
    df.to_csv(csv_file, mode='a', header=False, index=False)


def generator_initial_states(size_board, cant_initial_states):
    initial_states = []
    for i in range(cant_initial_states):
        sublist = random.sample(range(0, size_board**2), size_board**2)
        while sublist in initial_states or not n_puzzle_check_solvability(sublist):
            random.shuffle(sublist)
        initial_states.append(sublist)

    return initial_states


def get_initial_and_goal_states(row):
    split_states = row.split('"')
    init_state = split_states[1]
    goal_state = "[]"
    if len(split_states) > 3:
        goal_state = split_states[3]
    return init_state, goal_state


def problem_generator(list_initial):
    heuristics = [Heuristic.MANHATTAN, Heuristic.GASCHNIG, Heuristic.MISPLACED_NUMBERS, Heuristic.LINERAR_CONFLICT]
    algorithm_uniformed = list(UninformedAlgorithms)
    algorithm_uniformed.remove(UninformedAlgorithms.BIDIRECTIONAL_BREADTH_FIRST_SEARCH)
    algorithm_informed = list(InformedAlgorithms)
    for init in list_initial:
        for alg in algorithm_uniformed:
            add_row(Problems.NPUZZLE.name, alg.name, " ", " ", f'{init.__str__()}', int(sqrt(len(init))), " ",
                         "../n_puzzle_metrics_new.csv", "cfg_files/n_puzzle_new.csv")
        add_row(Problems.NPUZZLE.name, UninformedAlgorithms.BIDIRECTIONAL_BREADTH_FIRST_SEARCH.name, " ", " ",
                        f'{init.__str__()}', int(sqrt(len(init))), f'{n_puzzle_generate_goal_state(len(init))}',
                        "./n_puzzle_metrics/n_puzzle_metrics.csv", "cfg_files/n_puzzle.csv"
                     )
        for alg in algorithm_informed:
            for heu in heuristics:
                add_row(Problems.NPUZZLE.name, alg.name, " ", heu.name, f'{init.__str__()}', int(sqrt(len(init))), " ",
                             "./n_puzzle_metrics/n_puzzle_metrics.csv", "cfg_files/n_puzzle.csv")


def parse_n_puzzle(row):
    data = {}
    states = get_initial_and_goal_states(row)
    row = row.replace(states[0], '')
    if states[1] != "[]":
        row.replace(states[1], '')
    values = row.split(',')
    data["size"] = int(values[5])
    data["init_state"] = NPuzzleState(tuple(ast.literal_eval(states[0])), data["size"])
    data["goal_state"] = NPuzzleState(tuple(ast.literal_eval(states[1])), data["size"])
    data["problem"] = Problems.__members__[values[0]]
    data["algorithm"] = algorithm_parser(values[1])
    data["algorithm_params"] = values[2]
    data["heuristic"] = heuristic_parser(values[3])
    data["output_file"] = values[7]
    return data


if __name__ == "__main__":
    # string = "NPUZZLE,BREADTH_FIRST_SEARCH, , ,'[4, 2, 0, 1, 3, 8, 7, 6, 5]',3, ,../n_puzzle_metrics_new.csv"
    arg1 = sys.argv[1]
    main(arg1)
    # list_initial = generator_initial_states(3, 30)
    # list_initial.extend(generator_initial_states(4, 30))
    # list_initial.extend(generator_initial_states(5, 30))
    # list_initial.extend(generator_initial_states(6, 30))
    # list_initial.extend(generator_initial_states(7, 30))
    # list_initial.extend(generator_initial_states(8, 30))
    # list_initial.extend(generator_initial_states(9, 20))
    # list_initial.extend(generator_initial_states(10, 30))
    # list_initial.extend(generator_initial_states(11, 30))
    # list_initial.extend(generator_initial_states(12, 30))
    # list_initial.extend(generator_initial_states(13, 30))
    # list_initial.extend(generator_initial_states(14, 30))
    # list_initial.extend(generator_initial_states(15, 30))
    # problem_generator(list_initial)
