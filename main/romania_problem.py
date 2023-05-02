from random import random

from engine.engine import Engine
from engine.problems.practica_1.romania_map import romania_map
from main.utils import export_data


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


if __name__ == "__main__":
    # data = None
    # execute = Execute(data)
    # execute.main()
    romania_states_generator()
