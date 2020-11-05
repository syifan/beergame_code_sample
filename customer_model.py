class CustomerModel:

    def __init__(self):
        self.__demand = [
            4, 4, 4, 4, 4, 4, 8, 8,
            8, 8, 8, 8, 8, 8, 8, 8,
            4, 4, 4, 4, 4, 4, 4, 4,
        ]

    def customer_demand_at_round(self, round):
        return self.__demand[round]
