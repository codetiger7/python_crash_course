
class Restaurant:
    """A restaurant with a name and a cuisine"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " is a restaurant with a " +
              self.cuisine_type + " cuisine")

    @staticmethod
    def open_restaurant():
        print("The restaurant is open for business!")
