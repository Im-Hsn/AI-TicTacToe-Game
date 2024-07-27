from src.game import Game
from src.gui import GUI

def main():
    game = Game()
    gui = GUI(game)
    gui.run()

if __name__ == "__main__":
    main()