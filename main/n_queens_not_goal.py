import ast
import sys

import pandas as pd
from engine.engine import *
from main.utils import algorithm_parser, export_data, algorithm_name


class NQueensNotGoal:

    def __init__(self):
        self.data = None

    def main(self, data):
        split_states = data.split(',')
        if split_states[3] != " ":
            heuristic = "unattacked_squares"
        else:
            heuristic = "None"
        solution = {"problem": "NQueensProblem",
                    "algorithm": algorithm_name(split_states[1]),
                    "heuristic": heuristic,
                    "initial_state": str(tuple([-1] * int(split_states[4]))),
                    "goal_state": "None",
                    "depth": " ",
                    "explored_nodes": " ",
                    "generated_nodes": " ",
                    "Memory": " ",
                    "run_time": " ",
                    "path_cost": " ",
                    "path": " ",
                    "solution": " "
                    }
        export_data(solution, split_states[6])

    def import_data(self, file_name):
        self.data = pd.read_csv(file_name)


if __name__ == "__main__":
    # generated states
    # n_queens_problem_generator(n_queens_states_generator())

    n_queens_not_goal = NQueensNotGoal()
    arg1 = sys.argv[1]
    n_queens_not_goal.main(arg1)
