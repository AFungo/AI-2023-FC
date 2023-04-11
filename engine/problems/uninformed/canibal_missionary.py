from engine.problems.problem import Problem, Action, State



class CannibalMisionnary(Problem):

    def __init__(self, initial):
        self.initial = initial
        super().__init__([MoverC(), MoverM(), MoverCC(), MoverMM(), MoverCM()], self.initial)


class MoverC(Action):
    def is_enabled(self, state):
        cl, ml, cr, mr = state
        return ml >= cl > 0

    def execute(self, state):
        cl, ml, cr, mr = state
        return tuple([cl - 1, ml, cr + 1, mr])


class MoverM(Action):

    def is_enabled(self, state):
        cl, ml, cr, mr = state
        return ml > 0 and (cl == 1 and ml == 1)

    def execute(self, state):
        cl, ml, cr, mr = state
        return tuple([cl, ml - 1, cr, mr + 1])


class MoverCC(Action):

    def is_enabled(self, state):
        cl, ml, cr, mr = state
        return cl > 1 and cr + 2 <= mr

    def execute(self, state):
        cl, ml, cr, mr = state
        return tuple([cl - 2, ml, cr + 2, mr])


class MoverMM(Action):

    def is_enabled(self, state):
        cl, ml, cr, mr = state
        return ml > 1 and ml - 2 <= cl

    def execute(self, state):
        cl, ml, cr, mr = state
        return tuple([cl, ml - 2, cr, mr + 2])


class MoverCM(Action):

    def is_enabled(self, state):
        cl, ml, cr, mr = state
        return cl > 0 and ml > 0

    def execute(self, state):
        cl, ml, cr, mr = state
        return tuple([cl - 1, ml - 1, cr + 1, mr + 1])


class CannibalMissionaryState(State):

    def __init__(self, state):
        self.state = state
        self.ciudad_alaqu

    def is_goal(self):
        return self.state == self.ciuad

    def is_valid(self, state):
        cl, ml, cr, mr = state
        if cl < 0 or ml < 0 or cr < 0 or mr < 0:
            return False
        return True

    def is_loser(self, state):
        cl, ml, cr, mr = state
        return (cl > ml > 0) or (cr > mr > 0)
