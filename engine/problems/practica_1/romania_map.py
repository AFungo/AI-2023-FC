from engine.problems.abstract_problem import AbstractProblem, State, Actions
from engine.utils import UndirectedGraph, np, distance


class RomaniaMap(AbstractProblem):
    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal):
        actions_list = []
        for departure_city in romania_map.locations.keys():
            for arrival_city in romania_map.get(departure_city).keys():
                actions_list.append(RomaniaMapAction(departure_city, arrival_city))
        super().__init__(initial, action_list=actions_list, goal=goal)

    def path_cost(self, cost_so_far, A, action, B):
        return cost_so_far + (romania_map.get(A, B) or np.inf)

    def find_min_edge(self):
        """Find minimum value of edges."""
        m = np.inf
        for d in romania_map.graph_dict.values():
            local_min = min(d.values())
            m = min(m, local_min)

        return m


class RomaniaMapHeuristics:
    def __init__(self, goal_city):
        self.goal_city = goal_city

    def straigth_line_distance(self, node):
        """h function is straight-line distance from a node's state to goal."""
        locs = getattr(romania_map, 'locations', None)
        if locs:
            if type(node) is str:
                return int(distance(locs[node.state.city], locs[self.goal_city]))

            return int(distance(locs[node.state.city], locs[self.goal_city]))
        else:
            return np.inf


class RomaniaMapInverted(RomaniaMap):
    def __init__(self, initial):
        super().__init__(initial, goal=None)
        actions_list = []
        for departure_city in romania_map.locations.keys():
            for arrival_city in romania_map.get(departure_city).keys():
                actions_list.append(RomaniaMapActionInverted(departure_city, arrival_city))
        self.actions_list = actions_list


class RomaniaMapState(State):
    def __init__(self, city):
        self.city = city



    def __eq__(self, other):
        return isinstance(other, RomaniaMapState) and self.city == other.city

    def __hash__(self):
        return hash(self.city)

    def __lt__(self, other):
        return self

    def __str__(self):
        return self.city


class RomaniaMapAction(Actions):
    def __init__(self, departure_city, arrival_city):
        self.departure_city = departure_city
        self.arrival_city = arrival_city

    def is_enable(self, state):
        return romania_map.get(state.city).keys().__contains__(self.arrival_city) and state.city == self.departure_city

    def execute(self, state):
        return RomaniaMapState(self.arrival_city)

    def __str__(self):
        return "(" + self.departure_city + ", " + self.arrival_city + ")"


class RomaniaMapActionInverted:
    def __init__(self, departure_city, arrival_city):
        self.departure_city = departure_city
        self.arrival_city = arrival_city

    def is_enable(self, state):
        return romania_map.get(state.city).keys().__contains__(self.departure_city) and state.city == self.arrival_city

    def execute(self, state):
        return RomaniaMapState(self.departure_city)

    def __str__(self):
        return "(" + self.departure_city + ", " + self.arrival_city + ")"


romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))

romania_map.locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))
