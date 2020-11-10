from game import Game
from stage import Stage
from delivery import Delivery
from order import Order
from customer_model import CustomerModel


class GameController:

    def __init__(self, game: Game, customerModel: CustomerModel):
        self.__game = game
        self.__customer_model = customerModel

    def play(self):
        for i in range(self.__game.num_rounds):
            print(f"Round {i}")

            self.move_stacks()
            self.create_order_from_customer(i)

            stage_id = 0
            stage_to_stack_map = [(6, 10), (4, 12), (2, 14), (0, 16)]
            for stage in self.__game.stages:
                print(f"  Stage {stage.name}")
                self.check_delivery(stage)
                self.check_order(stage)
                self.deliver(stage, stage_to_stack_map[stage_id][1])
                self.make_order_decision(
                    stage, stage_to_stack_map[stage_id][0])

                stage_id += 1

    def create_order_from_customer(self, round):
        demand = self.__customer_model.customer_demand_at_round(round)
        order = Order(demand)
        self.__game.stages[3].receive_order(order)

    def move_stacks(self):
        game = self.__game

        game.stages[3].receive_delivery(game.stacks[15])
        game.stacks[15] = game.stacks[14]

        game.stages[2].receive_delivery(game.stacks[13])
        game.stacks[13] = game.stacks[12]

        game.stages[1].receive_delivery(game.stacks[11])
        game.stacks[11] = game.stacks[10]

        game.stages[0].receive_delivery(game.stacks[9])
        game.stacks[9] = game.stacks[8]

        d = Delivery(0)
        if game.stacks[7]:
            d.amount = game.stacks[7].amount
        game.stacks[8] = d

        game.stacks[7] = game.stacks[6]

        game.stages[0].receive_order(game.stacks[5])
        game.stacks[5] = game.stacks[4]

        game.stages[1].receive_order(game.stacks[3])
        game.stacks[3] = game.stacks[2]

        game.stages[2].receive_order(game.stacks[1])
        game.stacks[1] = game.stacks[0]

    def check_delivery(self, stage: Stage):
        print(f"    New delivery: {stage.current_supply}")
        print(f"    Current inventory level : {stage.inventory}")

    def check_order(self, stage: Stage):
        print(f"    New order: {stage.current_demand}")
        print(f"    Current backlog: {stage.backlog}")

    def deliver(self, stage: Stage, stackNumber):
        num_to_deliver = min(stage.inventory, stage.backlog)

        print(f"    Deliver {num_to_deliver}")
        stage.inventory -= num_to_deliver
        stage.backlog -= num_to_deliver

        d = Delivery(num_to_deliver)
        self.__game.stacks[stackNumber] = d

    def make_order_decision(self, stage: Stage, stackNumber):
        order_amount = int(input("How many unit to order?"))
        stage.order_to_make = order_amount

        o = Order(order_amount)
        self.__game.stacks[stackNumber] = o
