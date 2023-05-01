import pandas as pd

from engine.engine import *
from engine.problems.practica_1.n_puzzle import NPuzzleState


class Execute:
    def __init__(self):
        self.data = None

    def main(self, file_name):
        self.import_data(file_name)
        for i, row in self.data.iterrows():
            problem = Problems.__members__[row['problem']]
            algorithm = self.algorithm_parser(row['algorithm'])
            algorithm_params = row['algorithm_params']
            heuristic = Heuristic.__members__[row['heuristic']]
            problem_params = {"initial_state": NPuzzleState(tuple(row['initial_state']), row['n'])}
            goal_state = row['goal_state']
            engine = Engine(problem, algorithm, problem_params, heuristic, algorithm_params)
            solution = engine.solve()
            self.export_data(solution)

    def import_data(self, file_name):
        import ast
        self.data = pd.read_csv(file_name, converters={'initial_state': ast.literal_eval})

    def export_data(self, solution):
        print(solution.path())
        print(solution.solution())
        print(solution.path_cost)

    def algorithm_parser(self, name):
        try:
            algorithm = UninformedAlgorithms.__members__[name]
        except KeyError:
            try:
                algorithm = InformedAlgorithms.__members__[name]
            except KeyError:
                raise Exception("Algorithm not supported")
        return algorithm


if __name__ == "__main__":
    execute = Execute()
    execute.main("cfg_files/n_puzzle.csv")
