from random import random

from numpy.core._multiarray_umath import sqrt

from engine.engine import Engine, Heuristic, UninformedAlgorithms, Problems, InformedAlgorithms
from engine.problems.practica_1.romania_map import romania_map
from main.utils import export_data
import pandas as pd


class Execute:

    def __init__(self, data):
        self.data = data

    def main(self):
        d = self.data
        problem = None
        algorithm = None
        problem_params = None
        heuristic = None
        algorithm_params = None
        output_file = None
        engine = Engine(problem, algorithm, problem_params, heuristic, algorithm_params)
        solution = engine.solve()
        export_data(solution, output_file)


def romania_states_generator():
    states = list(romania_map.locations.keys())
    init_goal = []
    for i in range(50):
        new_state = (states[int(random()*len(states))], states[int(random()*len(states))])
        while new_state in init_goal or new_state[0] == new_state[1] or (new_state[1], new_state[0]) in init_goal:
            new_state = (states[int(random()*len(states))], states[int(random()*len(states))])
        init_goal.append(new_state)
    return init_goal

def romania_problem_generator(list_initial):
    data = {}
    heuristics = [Heuristic.STRAIGTH_LINE_DISTANCE]
    algorithm_uniformed = list(UninformedAlgorithms)
    algorithm_informed = list(InformedAlgorithms)
    for init in list_initial:
        for alg in algorithm_uniformed:
            data = {'problem': Problems.ROMANIA_MAP.name,
                    'algorithm': alg.name,
                    'algorithm_params': " ",
                    'heuristic': " ",
                    'initial_state': init[0],
                    'goal_state': init[1],
                    'output_file': "romania_map_metrics.csv"}
            df = pd.DataFrame(data, index=[0])
            df.to_csv('cfg_files/romania_map.csv', mode='a', header=False, index=False)
        for alg in algorithm_informed:
            for heu in heuristics:
                data = {'problem': Problems.ROMANIA_MAP.name,
                        'algorithm': alg.name,
                        'algorithm_params': " ",
                        'heuristic': heu.name,
                        'initial_state': init[0],
                        'goal_state': init[1],
                        'output_file': "romania_map_metrics.csv"}
                df = pd.DataFrame(data, index=[0])
                df.to_csv('cfg_files/romania_map.csv', mode='a', header=False, index=False)

if __name__ == "__main__":
    # data = None
    # execute = Execute(data)
    # execute.main()
    romania_problem_generator(romania_states_generator())
