from engine.problems import utils
from engine.problems.abstractproblem import *
from engine.problems.utils import is_tuple_ordered


class NPuzzle(MyProblem):
    """ The problem of sliding tiles numbered from 1 to n-1 on a nxn board, where one of the
    squares is a blank. A state is represented as a tuple of length n*n, where  element at
    index i represents the tile number  at index i (0 if it's an empty square) """

    def __init__(self, initial, n):
        """ Define goal state and initialize a problem """
        self.n = n
        actions_list = [NPuzzleMoveUp(n), NPuzzleMoveDown(n), NPuzzleMoveLeft(n), NPuzzleMoveRight(n)]
        super().__init__(initial, actions_list, None)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return state.is_goal()

    def check_solvability(self, state):
        """ Checks if the given state is solvable """

        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1

        return inversion % 2 == 0

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))


class NPuzzleState(State):
    def __init__(self, board):
        self.board = board

    def is_goal(self):
        return is_tuple_ordered(self.board)

    def find_blank_square(self):
        """Return the index of the blank square in a given state"""
        return self.board.index(0)


class NPuzzleMoveUp(Actions):
    def __init__(self, n):
        self.n = n

    def is_enable(self, state):
        index_blank_square = state.find_blank_square()
        return not index_blank_square < self.n

    def execute(self, state):
        delta = -self.n  # up
        return n_puzzle_move(state, delta)


class NPuzzleMoveDown(Actions):
    def __init__(self, n):
        self.n = n

    def is_enable(self, state):
        index_blank_square = state.find_blank_square()
        return not index_blank_square > ((self.n * self.n) - 1 - self.n)

    def execute(self, state):
        delta = self.n  # down
        return n_puzzle_move(state, delta)


class NPuzzleMoveLeft(Actions):
    def __init__(self, n):
        self.n = n

    def is_enable(self, state):
        index_blank_square = state.find_blank_square()
        return not index_blank_square % self.n == 0

    def execute(self, state):
        delta = -1  # left
        return n_puzzle_move(state, delta)


class NPuzzleMoveRight(Actions):
    def __init__(self, n):
        self.n = n

    def is_enable(self, state):
        index_blank_square = state.find_blank_square()
        return not index_blank_square % self.n == self.n - 1

    def execute(self, state):
        delta = 1  # right
        return n_puzzle_move(state, delta)


def n_puzzle_move(state, delta):
    """ Given state and action, return a new state that is the result of the action.
    Action is assumed to be a valid action in the state """
    # blank is the index of the blank square
    blank = state.find_blank_square()
    new_board = list(state.board)

    neighbor = blank + delta
    new_board[blank], new_board[neighbor] = new_board[neighbor], new_board[blank]

    return NPuzzleState(tuple(new_board))