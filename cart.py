# cart.py

class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product):
        self.items = [(p, q) for p, q in self.items if p != product]

    def get_items(self):
        return self.items

    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.get_price() * quantity
        return total
