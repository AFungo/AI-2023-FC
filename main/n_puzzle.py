import pandas as pd
import itertools
import random

from numpy.core._multiarray_umath import sqrt

from engine.engine import *
from engine.problems.practica_1.n_puzzle import NPuzzleState
from main.utils import export_data, algorithm_parser
from engine.engine import UninformedAlgorithms, InformedAlgorithms, Problems


class Execute:
    def __init__(self):
        self.data = None

    def main(self, file_name):
        self.import_data(file_name)
        for i, row in self.data.iterrows():
            problem = Problems.__members__[row['problem']]
            algorithm = algorithm_parser(row['algorithm'])
            algorithm_params = row['algorithm_params']
            heuristic = Heuristic.__members__[row['heuristic']]
            problem_params = {"initial_state": NPuzzleState(tuple(row['initial_state']), row['n'])}
            goal_state = row['goal_state']
            engine = Engine(problem, algorithm, problem_params, heuristic, algorithm_params)
            solution = engine.solve()
            export_data(solution, row["output_file"])

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


if __name__ == "__main__":
    execute = Execute()
    execute.problem_generator(execute.generator_initial_states(3, 20))
    execute.problem_generator(execute.generator_initial_states(4, 10))
    execute.problem_generator(execute.generator_initial_states(5, 10))
    execute.problem_generator(execute.generator_initial_states(6, 5))
    execute.problem_generator(execute.generator_initial_states(7, 5))
    # execute.main("cfg_files/n_puzzle.csv")
