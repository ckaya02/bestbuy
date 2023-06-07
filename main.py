def main():
    from store import Store
    from Products import Product
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250)]
    store = Store(product_list)
    products = store.get_all_products() #self.list_of_products=product_list
    def start():
        print("     Store Menu\n     _______\n1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit")

    while True:
        start()
        selection=int(input("Please choose a number: "))
        if selection!=1 and selection!=2 and selection!=3 and selection!=4:
            print("Please make a correct selection")
            input("Please enter to continue")
        if selection==3:
            orderlist = []
            while True:
                ordername=int(input("Which product # do you want? "))
                if ordername > len(products):
                    print("The order is not found")
                    input("Please enter to continue")
                else:
                    orderquantity=int(input("What amount do you want? "))
                    if orderquantity>product_list[0].quantity or orderquantity>product_list[1].quantity or orderquantity>product_list[2].quantity:
                        print(f'The ordered amount it too large')
                    orderlist.append((product_list[ordername-1], orderquantity))
                    print(f'Your total for {product_list[ordername-1].name} is:{product_list[ordername-1].price*orderquantity}')
                    totalprice=0
                    productnames=[]
                    for items, quant in orderlist:
                        totalprice += items.price * quant
                        items.buy(quant)
                        productnames.append(items.name)
                    print(f'Your current total for {productnames} is:{totalprice}')
                    cont=input("Do you want to continue shopping: Enter: Yes or No ")
                    yes="Yes"
                    if cont!=yes.lower():
                        break


        if selection==1:
            for i in range(len(product_list)):
                print(f'{i+1}. {products[i].name}, Price: ${product_list[i].price}, Quantity: {product_list[i].quantity}')
            input("Please enter to continue")
        if selection==2:
            total_quantity = 0
            for i in range(len(product_list)):
                total_quantity+=product_list[i].quantity
            print(total_quantity)
            input("Please enter to continue")
        if selection==4:
            break
if __name__ == "__main__":
        main()


