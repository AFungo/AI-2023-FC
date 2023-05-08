import ast
import sys

import pandas as pd
from engine.engine import *
from main.n_queens import parse_n_queens
from main.utils import algorithm_parser, export_data, algorithm_name


def add_row_no_goal(row):
    data = parse_n_queens(row)
    solution = parse_data_to_dictionary(data["problem"], data["algorithm"], data["heuristic"], data["number_of_queens"])
    export_data(solution, data["output_file"])

    def import_data(self, file_name):
        self.data = pd.read_csv(file_name)


if __name__ == "__main__":
    # generated states
    # n_queens_problem_generator(n_queens_states_generator())
    arg1 = sys.argv[1]
    add_row_no_goal(arg1)
