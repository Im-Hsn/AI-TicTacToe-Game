import numpy as np

class MiniMax:
    def __init__(self, game):
        self.game = game
        self.max_depth = np.inf

    def best_move(self):
        best_score = -np.inf
        move = None
        for row in range(3):
            for col in range(3):
                if self.game.board[row][col] == 0:
                    self.game.board[row][col] = 1
                    score = self.minimax(0, False)
                    self.game.board[row][col] = 0
                    if score > best_score:
                        best_score = score
                        move = (row, col)
        return move

    def minimax(self, depth, is_maximizing):
        if self.game.is_game_over(self.game.board) or depth == self.max_depth:
            return self.evaluate_board(self.game.board)

        if is_maximizing:
            best_score = -np.inf
            for row in range(3):
                for col in range(3):
                    if self.game.board[row][col] == 0:
                        self.game.board[row][col] = -1
                        score = self.minimax(depth + 1, False)
                        self.game.board[row][col] = 0
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = np.inf
            for row in range(3):
                for col in range(3):
                    if self.game.board[row][col] == 0:
                        self.game.board[row][col] = 1
                        score = self.minimax(depth + 1, True)
                        self.game.board[row][col] = 0
                        best_score = min(score, best_score)
            return best_score

    def evaluate_board(self, board):
        # Check rows, columns and diagonals for a win
        for row in range(3):
            row_sum = sum(board[row, :])
            if row_sum == 3:
                return 1000
            elif row_sum == -3:
                return -1000
            elif row_sum == 2:  # Two in a row with an open spot for AI
                return 800
            elif row_sum == -2:  # Two in a row with an open spot for opponent
                return -800

        for col in range(3):
            col_sum = sum(board[:, col])
            if col_sum == 3:
                return 1000
            elif col_sum == -3:
                return -1000
            elif col_sum == 2:  # Two in a column with an open spot for AI
                return 800
            elif col_sum == -2:  # Two in a column with an open spot for opponent
                return -800

        diag_sum = sum(board.diagonal())
        if diag_sum == 3:
            return 1000
        elif diag_sum == -3:
            return -1000
        elif diag_sum == 2:  # Two in a diagonal with an open spot for AI
                return 800
        elif diag_sum == -2:  # Two in a diagonal with an open spot for opponent
                return -800

        anti_diag_sum = sum(np.fliplr(board).diagonal())
        if anti_diag_sum == 3:
            return 1000
        elif anti_diag_sum == -3:
            return -1000
        elif anti_diag_sum == 2:  # Two in an anti-diagonal with an open spot for AI
                return 800
        elif anti_diag_sum == -2:  # Two in an anti-diagonal with an open spot for opponent
                return -800

        return 0  # Return 0 if there's no winner
