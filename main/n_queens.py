import ast
import sys

import pandas as pd
from engine.engine import *
from main.utils import algorithm_parser, export_data


class Execute:

    def __init__(self):
        self.data = None

    def main(self, data):
        split_states = data.split(',')
        # init_state = split_states[0]
        # # goal_state = "[]"
        # # if len(split_states) > 3:
        # #     goal_state = split_states[3]
        # #     data = data.replace(goal_state, '')
        # # data = data.replace(init_state, '')
        # # values = data.split(',')
        problem = Problems.__members__[split_states[0]]
        algorithm = algorithm_parser(split_states[1])
        algorithm_params = split_states[2]
        if split_states[3] != " ":
            heuristic = Heuristic.__members__[split_states[3]]
        else:
            heuristic = None
        aux = int(split_states[4])
        problem_params = {"number_queens": aux}
        # algorithm_params = {"goal_problem": NPuzzleInverted(NPuzzleState(tuple(ast.literal_eval(goal_state)), int(values[5])))}
        engine = Engine(problem, algorithm, problem_params, heuristic)
        solution = engine.solve()
        export_data(solution, split_states[6])

    def import_data(self, file_name):
        import ast
        self.data = pd.read_csv(file_name)


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
                    'output_file': "n_queens_metrics.csv"}
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
                        'output_file': "n_queens_metrics.csv"}
                df = pd.DataFrame(data, index=[0])
                df.to_csv('cfg_files/n_queens.csv', mode='a', header=False, index=False)


if __name__ == "__main__":

    execute = Execute()
    data = "N_QUEENS,BREADTH_FIRST_SEARCH, , ,4, ,n_queens_metrics.csv"
    # arg1 = sys.argv[1]
    execute.main(data)
    # execute.main("cfg_files/n_queens.csv")

    # n_queens_problem_generator(n_queens_states_generator())
