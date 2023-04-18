from engine.problems.abstractproblem import State, Actions, MyProblem


class NQueensProblem(MyProblem):

    def __int__(self, n):
        initial_state = NQueensState(n, tuple([-1] * n))
        actions_list = [Place_A_Queen_In_Board()]
        super().__init__(initial_state, actions_list, None)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return state.is_goal()


class NQueensState(State):

    def __init__(self, n, board):
        self.board = board
        self.n = n

    def is_goal(self):
        if self.board[-1] == -1:
            return False
        return not any(self.conflicted(self.board, self.board[col], col)
                       for col in range(len(self.board)))

    def conflicted(self, board, row, col):
        """Would placing a queen at (row, col) conflict with anything?"""
        return any(self.conflict(row, col, board[c], c)
                   for c in range(col))

    @staticmethod
    def conflict(row1, col1, row2, col2):
        """Would putting two queens in (row1, col1) and (row2, col2) conflict?"""
        return (row1 == row2 or  # same row
                col1 == col2 or  # same column
                row1 - col1 == row2 - col2 or  # same \ diagonal
                row1 + col1 == row2 + col2)  # same / diagonal


class Place_A_Queen_In_Board(Actions):

    def is_enable(self, state):
        col = state.index(-1)
        for row in range(state.N):
            if not self.conflicted(state, row, col):
                return True
        return False

    def conflicted(self, board, row, col):
        """Would placing a queen at (row, col) conflict with anything?"""
        return any(self.conflict(row, col, board[c], c)
                   for c in range(col))

    @staticmethod
    def conflict(row1, col1, row2, col2):
        """Would putting two queens in (row1, col1) and (row2, col2) conflict?"""
        return (row1 == row2 or  # same row
                col1 == col2 or  # same column
                row1 - col1 == row2 - col2 or  # same \ diagonal
                row1 + col1 == row2 + col2)  # same / diagonal

    def execute(self, state):
        """In the leftmost empty column, try all non-conflicting rows."""
        if state[-1] != -1:
            return []  # All columns filled; no successors
        else:
            col = state.index(-1)
            return [row for row in range(state.N)
                    if not self.conflicted(state, row, col)]
