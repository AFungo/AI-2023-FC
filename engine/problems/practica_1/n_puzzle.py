from engine.problems import utils
from engine.problems.abstract_problem import *
from engine.problems.utils import is_tuple_ordered


class NPuzzle(AbstractProblem):
    """ The problem of sliding tiles numbered from 1 to n-1 on a nxn board, where one of the
    squares is a blank. A state is represented as a tuple of length n*n, where  element at
    index i represents the tile number  at index i (0 if it's an empty square) """

    def __init__(self, initial):
        """ Define goal state and initialize a problem """
        self.n = initial.size
        actions_list = [NPuzzleMoveUp(self.n), NPuzzleMoveDown(self.n), NPuzzleMoveLeft(self.n), NPuzzleMoveRight(self.n)]
        super().__init__(initial, actions_list, None)


class NPuzzleState(State):
    def __init__(self, board, size):
        self.board = board
        self.index = 0
        self.size = size

    def is_goal(self):
        return is_tuple_ordered(self.board)

    def find_blank_square(self):
        """Return the index of the blank square in a given state"""
        return self.board.index(0)

    def __iter__(self):
        return self.board.__iter__()

    def __lt__(self, other):
        return self.board.__lt__(other.board)

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(self.board)

    def __str__(self):
        return str(self.board)


class NPuzzleMoveUp(Actions):
    def __init__(self, n):
        self.n = n

    def is_enable(self, state):
        index_blank_square = state.find_blank_square()
        return not index_blank_square < self.n

    def execute(self, state):
        delta = -self.n  # up
        return n_puzzle_move(state, delta)

    def __str__(self):
        return "Move up"


class NPuzzleMoveDown(Actions):
    def __init__(self, n):
        self.n = n

    def is_enable(self, state):
        index_blank_square = state.find_blank_square()
        return not index_blank_square > ((self.n * self.n) - 1 - self.n)

    def execute(self, state):
        delta = self.n  # down
        return n_puzzle_move(state, delta)

    def __str__(self):
        return "Move down"


class NPuzzleMoveLeft(Actions):
    def __init__(self, n):
        self.n = n

    def is_enable(self, state):
        index_blank_square = state.find_blank_square()
        return not index_blank_square % self.n == 0

    def execute(self, state):
        delta = -1  # left
        return n_puzzle_move(state, delta)

    def __str__(self):
        return "Move left"


class NPuzzleMoveRight(Actions):
    def __init__(self, n):
        self.n = n

    def is_enable(self, state):
        index_blank_square = state.find_blank_square()
        return not index_blank_square % self.n == self.n - 1

    def execute(self, state):
        delta = 1  # right
        return n_puzzle_move(state, delta)

    def __str__(self):
        return "Move right"


def n_puzzle_move(state, delta):
    """ Given state and action, return a new state that is the result of the action.
    Action is assumed to be a valid action in the state """
    # blank is the index of the blank square
    blank = state.find_blank_square()
    new_board = list(state.board)

    neighbor = blank + delta
    new_board[blank], new_board[neighbor] = new_board[neighbor], new_board[blank]

    return NPuzzleState(tuple(new_board), state.size)


class NPuzzleHeuristics:

    def misplaced_numbers(self, node):
        misplaced = 0
        board = node.state.board
        for i in range(len(board)):
            if board[i] != i + 1:
                misplaced += 1
        return misplaced

    def manhattan(self, node):
        distance = 0
        size = node.state.size
        board = node.state.board

        for i in range(size):
            for j in range(size):
                tile = board[i * size + j]
                if tile != 0:
                    gi, gj = (tile - 1) // size, (tile - 1) % size
                    distance += abs(i - gi) + abs(j - gj)
        return distance

    def linear_conflict(self, node):
        distance = 0
        size = node.state.size
        board = node.state.board
        for i in range(size):
            for j in range(size):
                tile = board[i * size + j]
                if tile != 0:
                    gi, gj = (tile - 1) // size, (tile - 1) % size
                    distance += abs(i - gi) + abs(j - gj)
                    if i != gi or j != gj:
                        distance += self.check_row(size, board, i, j, gi)
                        distance += self.check_column(size, board, i, j, gj)
        return distance

    def check_row(self, size, board, i, j, gi):
        distance = 0
        if i == gi:
            for k in range(size):
                tile_i = i * size + k
                tile = board[tile_i]
                goal_i = (tile - 1) // size
                if k != j and tile != 0 and goal_i == i:
                    distance += 2
        return distance

    def check_column(self, size, board, i, j, gj):
        distance = 0
        if j == gj:
            for k in range(size):
                tile_i = k * size + j
                tile = board[tile_i]
                goal_j = (tile - 1) % size
                if k != i and tile != 0 and goal_j == gj:
                    distance += 2
        return distance

    def gaschnig(self, node):
        state = node.state.board
        count = node.state.size
        for i in range(count):
            if state[i] == i + 1:
                count -= 1
            else:
                for j in range(i + 1, count):
                    if state[i] == j + 1 and state[j] == i + 1:
                        count -= 2
                        break
        return count


class NPuzzleInverted(NPuzzle):
    def __init__(self, initial):
        super().__init__(initial)
        self.actions_list = [NPuzzleMoveUpInverted(self.n), NPuzzleMoveDownInverted(self.n),
                             NPuzzleMoveLeftInverted(self.n), NPuzzleMoveRightInverted(self.n)]


class NPuzzleMoveUpInverted(NPuzzleMoveDown):
    def __str__(self):
        return "Move Up"


class NPuzzleMoveDownInverted(NPuzzleMoveUp):
    def __str__(self):
        return "Move Down"


class NPuzzleMoveLeftInverted(NPuzzleMoveRight):
    def __str__(self):
        return "Move Left"


class NPuzzleMoveRightInverted(NPuzzleMoveLeft):
    def __str__(self):
        return "Move Right"
