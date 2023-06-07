class Store:
    def __init__(self, list_of_products):
        self.list_of_products=list_of_products

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        self.list_of_products.remove(product)

    def get_total_quantity(self):
        total_quantity=0
        for product in self.list_of_products:
            total_quantity += product.get_quantity()
        return total_quantity
    def get_all_products(self):
        return self.list_of_products

    def order(self, shopping_list):
        total_price=0
        for product in shopping_list:
            total_price += product[0].price*product[1]
        return total_price