import ast
import re
import pandas as pd
import itertools
import random
import sys

from numpy.core._multiarray_umath import sqrt
from engine.engine import *
from engine.problems.practica_1.n_puzzle import NPuzzleState, NPuzzleInverted
from main.utils import export_data, algorithm_parser
from engine.engine import UninformedAlgorithms, InformedAlgorithms, Problems


class Execute:
    def __init__(self):
        self.data = None

    def main(self, data):
        split_states = data.split('"')
        init_state = split_states[1]
        goal_state = "[]"
        if len(split_states) > 3:
            goal_state = split_states[3]
            data = data.replace(goal_state, '')
        data = data.replace(init_state, '')
        values = data.split(',')
        problem = Problems.__members__[values[0]]
        algorithm = algorithm_parser(values[1])
        algorithm_params = values[2]
        if values[3] != " ":
            heuristic = Heuristic.__members__[values[3]]
        else:
            heuristic = None
        problem_params = {"initial_state": NPuzzleState(tuple(ast.literal_eval(init_state)), int(values[5]))}
        algorithm_params = {"goal_problem": NPuzzleInverted(NPuzzleState(tuple(ast.literal_eval(goal_state)), int(values[5])))}
        engine = Engine(problem, algorithm, problem_params, heuristic, algorithm_params=algorithm_params)
        solution = engine.solve()
        export_data(solution, values[7])

    def import_data(self, file_name):
        import ast
        self.data = pd.read_csv(file_name, converters={'initial_state': ast.literal_eval})

    def generator_initial_states(self, size_board, cant_initial_states):
        initial_states = []
        for i in range(cant_initial_states):
            sublist = random.sample(range(0, size_board**2), size_board**2)
            while sublist in initial_states:
                random.shuffle(sublist)
            initial_states.append(sublist)

        return initial_states

    def problem_generator(self, list_initial):
        data = {}
        heuristics = [Heuristic.MANHATTAN, Heuristic.GASCHNIG, Heuristic.MISPLACED_NUMBERS, Heuristic.LINERAR_CONFLICT]
        algorithm_uniformed = list(UninformedAlgorithms)
        algorithm_informed = list(InformedAlgorithms)
        for init in list_initial:
            for alg in algorithm_uniformed:
                data = {'problem': Problems.NPUZZLE.name,
                        'algorithm': alg.name,
                        'algorithm_params': " ",
                        'heuristic': " ",
                        'initial_state': f'{init.__str__()}',
                        'n': int(sqrt(len(init))),
                        'goal_state': " ",
                        'output_file': "n_puzzle_metrics.csv"}
                df = pd.DataFrame(data, index=[0])
                df.to_csv('cfg_files/n_puzzle.csv', mode='a', header=False, index=False)
            for alg in algorithm_informed:
                for heu in heuristics:
                    data = {'problem': Problems.NPUZZLE.name,
                            'algorithm': alg.name,
                            'algorithm_params': " ",
                            'heuristic': heu.name,
                            'initial_state': f'{init.__str__()}',
                            'n': int(sqrt(len(init))),
                            'goal_state': " ",
                            'output_file': "n_puzzle_metrics.csv"}
                    df = pd.DataFrame(data, index=[0])
                    df.to_csv('cfg_files/n_puzzle.csv', mode='a', header=False, index=False)


if __name__ == "__main__":
    execute = Execute()
    # string = "NPUZZLE,ASTAR_SEARCH, ,LINERAR_CONFLICT,'[2, 0, 6, 7, 5, 3, 4, 1, 8]',3, ,n_puzzle_metrics.csv"
    arg1 = sys.argv[1]
    execute.main(arg1)
