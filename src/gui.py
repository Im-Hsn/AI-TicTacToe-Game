import pygame
from src.alpha_beta import AlphaBeta
from src.minimax import MiniMax

# Defining the GUI class responsible for handling the game interface.
class GUI:
    def __init__(self, game):
        # Initializing pygame and setting up the game window.
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.game = game
        self.ai = None
        self.font = pygame.font.Font(None, 36)
        # Defining the positions and sizes of the algorithm selection buttons.
        self.algorithm_buttons = {
            "Minimax": pygame.Rect(50, 250, 200, 50),
            "Alpha-Beta": pygame.Rect(350, 250, 200, 50)
        }

    # Method to draw the algorithm selection buttons on the screen.
    def draw_algorithm_buttons(self):
        colors = {"Minimax": (0, 0, 255), "Alpha-Beta": (255, 0, 0)}
        for algorithm, rect in self.algorithm_buttons.items():
            pygame.draw.rect(self.screen, colors[algorithm], rect)
            text = self.font.render(algorithm, True, (255, 255, 255))
            text_rect = text.get_rect(center=rect.center)
            self.screen.blit(text, text_rect)

    # Method to draw the Tic Tac Toe board on the screen.
    def draw_board(self):
        for row in range(3):
            for col in range(3):
                if self.game.board[row][col] == 1:
                    pygame.draw.circle(self.screen, (0, 0, 255), (col * 200 + 100, row * 200 + 100), 90, 15)
                elif self.game.board[row][col] == -1:
                    pygame.draw.line(self.screen, (255, 0, 0), (col * 200 + 30, row * 200 + 170), (col * 200 + 170, row * 200 + 30), 15)
                    pygame.draw.line(self.screen, (255, 0, 0), (col * 200 + 30, row * 200 + 30), (col * 200 + 170, row * 200 + 170), 15)
        # Drawing grid lines for the Tic Tac Toe board.
        for i in range(1, 3):
            pygame.draw.line(self.screen, (0, 0, 0), (i * 200, 0), (i * 200, 600), 5)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 200), (600, i * 200), 5)

    # Method to draw outlined text on the screen.
    def draw_outlined_text(self, text, font, color, center):
        main_text_surface = font.render(text, True, color)
        outline_text_surface = font.render(text, True, (0, 0, 0))
        main_text_rect = main_text_surface.get_rect(center=center)
        outline_text_rect = main_text_rect.copy()
        outline_text_rect.topleft = (main_text_rect.left - 2, main_text_rect.top - 2)
        self.screen.blit(outline_text_surface, outline_text_rect)
        self.screen.blit(main_text_surface, main_text_rect)

    # Method to run the game loop.
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.ai is None:
                        for algorithm, rect in self.algorithm_buttons.items():
                            # Checking if an algorithm button was clicked.
                            if rect.collidepoint(pos):
                                # Initializing AI based on selected algorithm.
                                if algorithm == "Minimax":
                                    self.ai = MiniMax(self.game)
                                elif algorithm == "Alpha-Beta":
                                    self.ai = AlphaBeta(self.game)
                    else:
                        row, col = pos[1] // 200, pos[0] // 200
                        # Making a move on the game board.
                        if self.game.make_move(row, col):
                            # If game is not over, AI makes its move.
                            if not self.game.is_game_over():
                                ai_move = self.ai.best_move()
                                self.game.make_move(*ai_move)
            self.screen.fill((255, 255, 255))
            # If AI is not initialized, draw algorithm selection buttons.
            if self.ai is None:
                self.draw_algorithm_buttons()
            else:
                # If AI is initialized, draw the Tic Tac Toe board.
                self.draw_board()
                # Check if the game is over and display the winner.
                if self.game.is_game_over():
                    winner = self.game.get_winner()
                    if winner == -1:
                        self.draw_outlined_text("AI wins!", self.font, (128, 0, 128), (300, 300))
                    elif winner == 1:
                        self.draw_outlined_text("Player wins!", self.font, (128, 0, 128), (300, 300))
                    else:
                        self.draw_outlined_text("It's a draw!", self.font, (128, 0, 128), (300, 300))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    running = False
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()