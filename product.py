# product.py

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description
