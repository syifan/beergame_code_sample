from game import Game
from stage import Stage


class GameController:

    def __init__(self, game: Game):
        self.__game = game

    def play(self):
        for i in range(self.__game.num_rounds):
            print(f"Round {i}")

            for stage in self.__game.stages:
                print(f"  Stage {stage.name}")
                self.check_delivery(stage)
                self.check_order(stage)
                self.deliver(stage)
                self.make_order_decision(stage)

    def check_delivery(self, stage: Stage):
        print(f"    New delivery: {stage.current_supply}")
        print(f"    Current inventory level : {stage.inventory}")

    def check_order(self, stage: Stage):
        print(f"    New order: {stage.current_demand}")
        print(f"    Current backlog: {stage.backlog}")

    def deliver(self, stage: Stage):
        num_to_deliver = max(stage.inventory, stage.backlog)

        print(f"    Deliver {num_to_deliver}")
        stage.inventory -= num_to_deliver
        stage.backlog -= num_to_deliver

    def make_order_decision(self, stage: Stage):
        order_amount = input("How many unit to order?")
        stage.order_to_make = order_amount
