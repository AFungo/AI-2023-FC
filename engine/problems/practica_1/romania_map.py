from engine.problems.abstractproblem import MyProblem, State, Actions
from engine.utils import UndirectedGraph, np, distance


class RomaniaMap(MyProblem):
    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal):
        actions_list = []
        for city in romania_map.locations.keys():
            actions_list.append(RomaniaMapAction(city))
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

    def h(self, node):
        """h function is straight-line distance from a node's state to goal."""
        locs = getattr(romania_map, 'locations', None)
        if locs:
            if type(node) is str:
                return int(distance(locs[node], locs[self.goal]))

            return int(distance(locs[node.state], locs[self.goal]))
        else:
            return np.inf


class RomaniaMapState(State):
    def __init__(self, city):
        self.city = city

    def __eq__(self, other):
        return isinstance(other, RomaniaMapState) and self.city == other.city

    def __hash__(self):
        return hash(self.city)


class RomaniaMapAction(Actions):
    def __init__(self, arrival_city):
        self.arrival_city = arrival_city

    def is_enable(self, state):
        return romania_map.get(state.city).keys().__contains__(self.arrival_city)

    def execute(self, state):
        return RomaniaMapState(self.arrival_city)

    def __str__(self):
        return self.arrival_city


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