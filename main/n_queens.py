import pandas as pd
from engine.engine import *
from main.utils import algorithm_parser, export_data


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
            problem_params = {"number_queens": row['n']}
            goal_state = row['goal_state']
            engine = Engine(problem, algorithm, problem_params, heuristic, algorithm_params)
            solution = engine.solve()
            export_data(solution, row["output_file"])

    def import_data(self, file_name):
        import ast
        self.data = pd.read_csv(file_name)


def n_queens_states_generator():
    states = []
    for i in range(50):
        states.append(i)
    return states


if __name__ == "__main__":
    execute = Execute()
    execute.main("cfg_files/n_queens.csv")
