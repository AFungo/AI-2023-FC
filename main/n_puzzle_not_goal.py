import sys

from main.n_puzzle import parse_n_puzzle
from main.utils import parse_data_to_dictionary, export_data


def add_row_no_goal(row):
    data = parse_n_puzzle(row)
    solution = parse_data_to_dictionary(data["problem"], data["algorithm"], data["heuristic"], data["init_state"])
    export_data(solution, data["output_file"])

if __name__ == "__main__":
#    arg1 = sys.argv[1]
    string = "NPUZZLE,BREADTH_FIRST_SEARCH, , ,\"[4, 2, 0, 1, 3, 8, 7, 6, 5]\",3, ,../n_puzzle_metrics_new.csv"
    add_row_no_goal(string)
