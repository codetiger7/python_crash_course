from car import Car
from battery import Battery


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parents class."""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """No gas tank in electric cars"""
        print("This car doesn't need a gas tank")

