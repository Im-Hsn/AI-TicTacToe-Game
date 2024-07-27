import numpy as np

class Game:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.current_player = 1

    def make_move(self, row, col):
        if self.board[row][col] == 0:
            self.board[row][col] = self.current_player
            self.current_player = -1 if self.current_player == 1 else 1
            return True
        return False
    
    def get_winner(self, board=None):
        board = self.board if board is None else board
        # Check rows, columns and diagonals for a win
        for i in range(3):
            if abs(sum(self.board[i, :])) == 3:
                return self.board[i, 0]
            if abs(sum(self.board[:, i])) == 3:
                return self.board[0, i]
        if abs(sum(self.board.diagonal())) == 3:
            return self.board[0, 0]
        if abs(sum(np.fliplr(self.board).diagonal())) == 3:
            return self.board[0, 2]
        return 0  # Return 0 if there's no winner


    def is_game_over(self, board=None):
        board = self.board if board is None else board
        # Check rows, columns and diagonals for a win
        for i in range(3):
            if abs(sum(self.board[i, :])) == 3 or abs(sum(self.board[:, i])) == 3:
                return True
        if abs(sum(self.board.diagonal())) == 3 or abs(sum(np.fliplr(self.board).diagonal())) == 3:
            return True
        # Check if the board is full
        if not 0 in self.board:
            return True
        return False
