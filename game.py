
# First way to import a module
#

# Third way to import a module
from stage import Manufacturer, Distributer, Retailer


class Game:

    def __init__(self):
        self.num_rounds = 24
        self.stages = []

        self.stages.append(Manufacturer("Manufacturer"))
        self.stages.append(Distributer("Distributor"))
        self.stages.append(Distributer("Wholesaler"))
        self.stages.append(Retailer("Retailer"))
