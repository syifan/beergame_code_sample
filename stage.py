class Stage:

    def __init__(self, name):
        self.name = name
        self.backlog = 0
        self.inventory = 0
        self.current_supply = 0
        self.current_demand = 0
        self.order_to_make = 0

    def receive_delivery(self, delivery):
        self.current_supply = 0
        if delivery:
            self.current_supply = delivery.amount
            self.inventory += delivery.amount

    def receive_order(self, order):
        self.current_demand = 0
        if order:
            self.current_demand = order.amount
            self.backlog += order.amount


class Manufacturer(Stage):
    pass


class Distributer(Stage):
    pass


class Retailer(Stage):
    pass
