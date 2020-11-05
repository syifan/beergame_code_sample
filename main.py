from game import Game
from game_controller import GameController


def main():
    game = Game()
    controller = GameController(game)

    controller.play()


if __name__ == "__main__":
    main()
