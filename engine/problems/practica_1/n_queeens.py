from engine.problems.abstractproblem import State, Actions, MyProblem


class NQueensProblem(MyProblem):

    def __init__(self, n):
        initial_state = NQueensState(n, tuple([-1] * n))
        actions_list = []
        for i in range(n):
            for j in range(n):
                actions_list.append(Place_A_Queen_In_Board(i, j))
        super().__init__(initial_state, actions_list)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return state.is_goal()


class NQueensState(State):

    def __init__(self, n, board):
        self.board = board
        self.n = n

    def is_goal(self):
        for i in range(self.n):
            if self.board[i] == -1:
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

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def is_enable(self, state):
        return not self.conflicted(state, self.row, self.col)

        # col = state.board.index(-1)
        # for row in range(state.n):
        #     if not self.conflicted(state, row, col):
        #         return True
        # return False

    def conflicted(self, state, row, col):
        """Would placing a queen at (row, col) conflict with anything?"""
        return any(self.conflict(row, col, state.board[c], c)
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
        if self.is_enable(state):
            new_board = list(state.board)
            new_board[self.col] = self.row
            return NQueensState(state.n, tuple(new_board))
        return ()
