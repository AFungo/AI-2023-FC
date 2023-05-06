from engine.utils import is_in


class Problems:

    def goal_state(self):
        """Return the goal state."""
        raise NotImplementedError

    def initial_state(self):
        raise NotImplementedError

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        raise NotImplementedError

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2. If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        raise NotImplementedError

    def value(self, state):
        raise NotImplementedError


class AbstractProblem(Problems):

    def __init__(self, initial, action_list, goal=None):
        self.goal = goal
        self.actions_list = action_list
        self.initial = initial

    def initial_state(self):
        return self.initial

    def goal_state(self):
        return self.goal

    def actions(self, state):
        return list(filter(lambda a: a.is_enable(state), self.actions_list))

    def result(self, state, action):
        new_state = action.execute(state)
        return new_state

    def goal_test(self, state):
        try:
            return state.is_goal()
        except NotImplementedError:
            if isinstance(self.goal, list):
                return is_in(state, self.goal)
            else:
                return state == self.goal

    def path_cost(self, c, state1, action, state2):
        return c + 1

    def value(self, state):
        raise NotImplementedError


class CountNodes(Problems):

    def __init__(self, problem):
        self.problem = problem
        self.explored_node = 0
        self.generated_nodes = 0

    def goal_state(self):
        return self.problem.goal_state()

    def initial_state(self):
        return self.problem.initial_state()

    def actions(self, state):
        return self.problem.actions(state)

    def result(self, state, action):
        self.generated_nodes += 1
        return self.problem.result(state, action)

    def goal_test(self, state):
        self.explored_node += 1
        return self.problem.goal_test(state)

    def path_cost(self, c, state1, action, state2):
        return self.problem.path_cost(c, state1, action, state2)

    def value(self, state):
        return self.problem.value(state)


class State:
    def is_goal(self):
        """Return True if the state is a goal."""
        raise NotImplementedError

    def rep_ok(self):
        raise NotImplementedError


class Actions:
    def is_enable(self, state):
        raise NotImplementedError

    def execute(self, state):
        raise NotImplementedError
