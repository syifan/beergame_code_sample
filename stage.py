class Stage:

    def __init__(self, name):
        self.name = name
        self.backlog = 0
        self.inventory = 0
        self.current_supply = 0
        self.current_demand = 0
        self.order_to_make = 0


class Manufacturer(Stage):
    pass


class Distributer(Stage):
    pass


class Retailer(Stage):
    pass
