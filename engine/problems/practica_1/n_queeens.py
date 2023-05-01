from engine.problems.abstractproblem import State, Actions, MyProblem


class NQueensProblem(MyProblem):

    def __init__(self, n):
        initial_state = NQueensState(n, tuple([-1] * n))
        actions_list = []
        for col in range(n):
            for row in range(n):
                actions_list.append(Place_A_Queen_In_Board(col, row))
        super().__init__(initial_state, actions_list)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return state.is_goal()

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is
        h(n) = number of misplaced tiles """
        h = 0
        board = node.state.board
        for i in range(len(board)):
            if board[i] != i + 1:
                h += 1
        return h
        # return sum(s != g for (s, g) in zip(n, node.state))


class NQueensHeuristics:

    def unattacked_squares(self, node):
        not_attack = 0
        try:
            current_col = node.state.board.index(-1)
            for col in range(current_col, node.state.n):
                for row in range(node.state.n):
                    if not self.conflicted(node.state.board, row, col):
                        not_attack += 1
        except ValueError:
            return not_attack
        return not_attack

    def least_attacked_col(self, node):
        col_attackeds = []
        try:
            current_col = node.state.board.index(-1)
            for col in range(current_col, node.state.n):
                col_attacked = 0
                for row in range(node.state.n):
                    if not self.conflicted(node.state.board, row, col):
                        col_attacked += 1
                col_attackeds.append(col_attacked)
        except ValueError:
            return 0
        return min(col_attackeds)

    def conflicted(self, board, row, col):
        """Would placing a queen at (row, col) conflict with anything?"""
        return any(self.conflict(row, col, board[c], c)
                   for c in range(col))

    def conflict(self, row1, col1, row2, col2):
        """Would putting two queens in (row1, col1) and (row2, col2) conflict?"""
        return (row1 == row2 or  # same row
                col1 == col2 or  # same column
                row1 - col1 == row2 - col2 or  # same \ diagonal
                row1 + col1 == row2 + col2)  # same / diagonal


class NQueensState(State):

    def __init__(self, n, board):
        self.board = board
        self.n = n

    def __lt__(self, other):
        return self.board.__lt__(other.board)

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

    def __init__(self, col, row):
        self.col = col
        self.row = row

    def is_enable(self, state):
        return not self.conflicted(state, self.row, self.col) and self.check_order(state)

    def check_order(self, state):
        if self.col > 0:
            return state.board[self.col - 1] != -1
        elif self.col == 0:
            return state.board[self.col] == -1
        else:
            Exception("Invalid index")

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
        if self.is_enable(state):
            new_board = list(state.board)
            new_board[self.col] = self.row
            return NQueensState(state.n, tuple(new_board))
        return ()
