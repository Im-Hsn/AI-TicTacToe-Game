import numpy as np

class AlphaBeta:
    def __init__(self, game):
        self.game = game

    def evaluate(self, board):
        winner = self.game.get_winner(board)
        if winner == 1:
            return 10
        elif winner == -1:
            return -10
        else:
            return 0

    def minimax(self, board, depth, is_max_player, alpha, beta):
        winner = self.game.get_winner(board)
        if winner != 0 or depth == 0 or self.game.is_game_over(board):
            return self.evaluate(board)

        if is_max_player:
            max_eval = -np.inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == 0:
                        board[row][col] = -1
                        eval = self.minimax(board, depth - 1, False, alpha, beta)
                        board[row][col] = 0
                        max_eval = max(eval, max_eval)
                        alpha = max(alpha, eval)
                        if beta <= alpha:
                            break
            return max_eval

        else:
            min_eval = np.inf
            for row in range(3):
                for col in range(3):
                    if board[row][col] == 0:
                        board[row][col] = 1
                        eval = self.minimax(board, depth - 1, True, alpha, beta)
                        board[row][col] = 0
                        min_eval = min(eval, min_eval)
                        beta = min(beta, eval)
                        if beta <= alpha:
                            break
            return min_eval
        
    def best_move(self):
        best_move = None
        best_score = -np.inf
        depth = sum(x == 0 for row in self.game.board for x in row)  # Count the number of empty spots

        for row in range(3):
            for col in range(3):
                if self.game.board[row][col] == 0:
                    self.game.board[row][col] = 1
                    score = self.minimax(self.game.board, depth, False, -np.inf, np.inf)
                    self.game.board[row][col] = 0
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move  # Return only the best move
