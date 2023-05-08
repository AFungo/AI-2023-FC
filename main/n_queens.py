import ast
import sys

import pandas as pd
from engine.engine import *
from main.utils import algorithm_parser, export_data, heuristic_parser


def main(row):
    data = parse_n_queens(row)
    problem_params = {"number_queens": data["number_of_queens"]}
    engine = Engine(data["problem"], data["algorithm"], problem_params, data["heuristic"])
    solution = engine.solve()
    export_data(solution, data["output_file"])


def parse_n_queens(row):
    data = {}
    split_states = row.split(',')
    data["problem"] = Problems.__members__[split_states[0]]
    data["algorithm"] = algorithm_parser(split_states[1])
    data["heuristic"] = heuristic_parser(split_states[3])
    data["number_of_queens"] = int(split_states[4])
    data["output_file"] = split_states[6]
    return data


def n_queens_states_generator():
    states = []
    for i in range(4, 54):
        states.append(i)
    return states


def n_queens_problem_generator(list_initial):
    data = {}
    heuristics = [Heuristic.UNATTACHED_SQUARES]
    algorithm_uniformed = list(UninformedAlgorithms)
    algorithm_uniformed.remove(UninformedAlgorithms.BIDIRECTIONAL_BREADTH_FIRST_SEARCH)
    algorithm_informed = list(InformedAlgorithms)
    for init in list_initial:
        for alg in algorithm_uniformed:
            data = {'problem': Problems.N_QUEENS.name,
                    'algorithm': alg.name,
                    'algorithm_params': " ",
                    'heuristic': " ",
                    'number_queens': init,
                    'goal_state': " ",
                    'output_file': "./n_queens_metrics/n_queens_metrics.csv"}
            df = pd.DataFrame(data, index=[0])
            df.to_csv('cfg_files/n_queens.csv', mode='a', header=False, index=False)

        for alg in algorithm_informed:
            for heu in heuristics:
                data = {'problem': Problems.N_QUEENS.name,
                        'algorithm': alg.name,
                        'algorithm_params': " ",
                        'heuristic': heu.name,
                        'number_queens': init,
                        'goal_state': " ",
                        'output_file': "./n_queens_metrics/n_queens_metrics.csv"}
                df = pd.DataFrame(data, index=[0])
                df.to_csv('cfg_files/n_queens.csv', mode='a', header=False, index=False)


if __name__ == "__main__":

    # generated states
    # n_queens_problem_generator(n_queens_states_generator())

    arg1 = sys.argv[1]
    main(arg1)
