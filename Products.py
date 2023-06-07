class Product:
    def __init__(self, name, price, quantity, active=True):
            self.name=str(name)
            self.price=float(price)
            self.quantity=int(quantity)
            self.active=active

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity==0:
           self.deactivate()
        return self.quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.active=True

    def deactivate(self):
        self.active=False

    def show(self):
        return f'Name= {self.name},price: {self.price}, quantity: {self.quantity}'

    def buy(self, buyquantity):
        total=buyquantity*self.price
        self.quantity-=buyquantity
        return total, self.quantity