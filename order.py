# order.py

class Order:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer
        self.paid = False

    def get_cart(self):
        return self.cart

    def get_customer(self):
        return self.customer

    def is_paid(self):
        return self.paid

    def process_payment(self):
        # 实际的支付处理逻辑
        self.paid = True
