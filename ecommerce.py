# ecommerce.py

from product import Product
from cart import Cart
from order import Order

class EcommerceApp:
    def __init__(self):
        self.products = []
        self.orders = []

    def create_product(self, name, price, description):
        product = Product(name, price, description)
        self.products.append(product)
        return product

    def create_cart(self):
        cart = Cart()
        return cart

    def create_order(self, cart, customer):
        order = Order(cart, customer)
        self.orders.append(order)
        return order

    def get_products(self):
        return self.products

    def get_orders(self):
        return self.orders
