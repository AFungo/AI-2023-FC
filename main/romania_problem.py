import sys
from random import random

from numpy.core._multiarray_umath import sqrt

from engine.engine import Engine, Heuristic, UninformedAlgorithms, Problems, InformedAlgorithms
from engine.problems.practica_1.romania_map import romania_map, RomaniaMapState, RomaniaMapInverted
from main.utils import export_data, algorithm_parser
import pandas as pd


class Execute:

    def main(self, data):
        values = data.split(',')
        problem = Problems.__members__[values[0]]
        algorithm = algorithm_parser(values[1])
        if values[3] != " ":
            heuristic = Heuristic.__members__[values[3]]
        else:
            heuristic = None
        problem_params = {"initial_state": RomaniaMapState(values[4]), "goal_state": RomaniaMapState(values[5])}
        algorithm_params = {"goal_problem": RomaniaMapInverted(RomaniaMapState(values[5]))}
        output_file = values[6]
        heuristic_params = {"goal_city": values[5]}
        engine = Engine(problem, algorithm, problem_params, heuristic, algorithm_params, heuristic_params=heuristic_params)
        solution = engine.solve()
        export_data(solution, output_file)


def romania_states_generator():
    states = list(romania_map.locations.keys())
    init_goal = []
    for i in range(100):
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
                    'output_file': "./romania_map_metrics/romania_map_metrics.csv"}
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
                        'output_file': "./romania_map_metrics/romania_map_metrics.csv"}
                df = pd.DataFrame(data, index=[0])
                df.to_csv('cfg_files/romania_map.csv', mode='a', header=False, index=False)

if __name__ == "__main__":
    #    romania_problem_generator(romania_states_generator())
    # data = "N_QUEENS,ASTAR_SEARCH, ,UNATTACHED_SQUARES,4, ,../n_queens_metrics/n_queens_metrics.csv"
    execute = Execute()
    arg1 = sys.argv[1]
    execute.main(arg1)
    # string = "ROMANIA_MAP,BIDIRECTIONAL_BREADTH_FIRST_SEARCH, , ,Iasi,Vaslui,./romania_map_metrics/romania_map_metrics.csv"
    # execute.main(string)

