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
    for i in range(4, 54):
        states.append(i)
    return states


def n_queens_problem_generator(list_initial):
    data = {}
    heuristics = [Heuristic.UNATTACHED_SQUARES]
    algorithm_uniformed = list(UninformedAlgorithms)
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
    # execute = Execute()
    # execute.main("cfg_files/n_queens.csv")
    n_queens_problem_generator(n_queens_states_generator())
