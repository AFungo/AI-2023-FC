import ast
import re
import pandas as pd
import itertools
import random
import sys

from numpy.core._multiarray_umath import sqrt
from engine.engine import *
from engine.problems.practica_1.n_puzzle import NPuzzleState, NPuzzleInverted
from main.utils import export_data, algorithm_parser, n_puzzle_check_solvability, n_puzzle_generate_goal_state
from engine.engine import UninformedAlgorithms, InformedAlgorithms, Problems


class Execute:

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

    def generator_initial_states(self, size_board, cant_initial_states):
        initial_states = []
        for i in range(cant_initial_states):
            sublist = random.sample(range(0, size_board**2), size_board**2)
            while sublist in initial_states or not n_puzzle_check_solvability(sublist):
                random.shuffle(sublist)
            initial_states.append(sublist)

        return initial_states

    def add_row(self, problem, algorithm, algorithm_params, heuristic, initial_state, n, goal_state, output_file, csv_file):
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

    def problem_generator(self, list_initial):
        data = {}
        heuristics = [Heuristic.MANHATTAN, Heuristic.GASCHNIG, Heuristic.MISPLACED_NUMBERS, Heuristic.LINERAR_CONFLICT]
        algorithm_uniformed = list(UninformedAlgorithms)
        algorithm_uniformed.remove(UninformedAlgorithms.BIDIRECTIONAL_BREADTH_FIRST_SEARCH)
        algorithm_informed = list(InformedAlgorithms)
        for init in list_initial:
            for alg in algorithm_uniformed:
                self.add_row(Problems.NPUZZLE.name, alg.name, " ", " ", f'{init.__str__()}', int(sqrt(len(init))), " ",
                             "../n_puzzle_metrics_new.csv", "cfg_files/n_puzzle_new.csv")
            self.add_row(Problems.NPUZZLE.name, UninformedAlgorithms.BIDIRECTIONAL_BREADTH_FIRST_SEARCH.name, " ", " ",
                            f'{init.__str__()}', int(sqrt(len(init))), f'{n_puzzle_generate_goal_state(len(init))}',
                            "../n_puzzle_metrics_new.csv", "cfg_files/n_puzzle_new.csv"
                         )
            for alg in algorithm_informed:
                for heu in heuristics:
                    self.add_row(Problems.NPUZZLE.name, alg.name, " ", heu.name, f'{init.__str__()}', int(sqrt(len(init))), " ",
                                 "../n_puzzle_metrics_new.csv", "cfg_files/n_puzzle_new.csv")


if __name__ == "__main__":
    execute = Execute()
    # string = "NPUZZLE,GREEDY_BEST_FIRST_SEARCH, ,MANHATTAN,'[3, 1, 7, 4, 2, 5, 8, 6, 0]',3, ,../n_puzzle_metrics_new.csv"
    arg1 = sys.argv[1]
    execute.main(arg1)
    # list_initial = execute.generator_initial_states(3, 10)
    # list_initial.extend(execute.generator_initial_states(4, 10))
    # list_initial.extend(execute.generator_initial_states(5, 10))
    # list_initial.extend(execute.generator_initial_states(6, 10))
    # list_initial.extend(execute.generator_initial_states(7, 10))
    # list_initial.extend(execute.generator_initial_states(8, 10))
    # list_initial.extend(execute.generator_initial_states(9, 10))
    # list_initial.extend(execute.generator_initial_states(10, 10))
    # list_initial.extend(execute.generator_initial_states(11, 10))
    # list_initial.extend(execute.generator_initial_states(12, 10))
    # list_initial.extend(execute.generator_initial_states(13, 10))
    # list_initial.extend(execute.generator_initial_states(14, 10))
    # list_initial.extend(execute.generator_initial_states(15, 10))
    # execute.problem_generator(list_initial)
