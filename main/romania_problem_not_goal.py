import ast
import sys

import pandas as pd
from engine.engine import *
from main.romania_problem import parse_romania_problem
from main.utils import algorithm_parser, export_data, algorithm_name


def add_row_no_goal(row):
    data = parse_romania_problem(row)
    solution = parse_data_to_dictionary(data["problem"], data["algorithm"], data["heuristic"],
                                        data["departure_city"])
    export_data(solution, data["output_file"])


if __name__ == "__main__":
    # generated states
    # n_queens_problem_generator(n_queens_states_generator())

    arg1 = sys.argv[1]
    add_row_no_goal(arg1)
