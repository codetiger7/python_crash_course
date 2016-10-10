from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Model ice cream stand"""

    def __init__(self, restaurant_name):
        super().__init__(restaurant_name, cuisine_type="Ice Cream Stand")
        self.flavours = ['strawberry', 'blueberry', 'chocolate',
                         'raspberry', 'apple', 'mango', 'pear', 'pineapple']

    def display_flavours(self):
        for flavour in self.flavours:
            print(flavour)


