from game import Game
from game_controller import GameController
from customer_model import CustomerModel


def main():
    game = Game()
    cm = CustomerModel()
    controller = GameController(game, cm)

    controller.play()


if __name__ == "__main__":
    main()
