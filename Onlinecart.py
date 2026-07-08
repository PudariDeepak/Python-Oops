#Writing a program how to add,delete and updates to the cart and printing the total amount
class Cart:
    def __init__(self):
        self.products={"Shirt":600,"Pant":900,"T-shirt":300,"Shoe":1000}
        self.cart={}

    def add_items(self,item):
        self.cart[item]=1

    def update_items(self,item,quantity):
        self.cart[item]=quantity

    def remove_items(self,item):
        self.cart.pop(item)

    def view_cart(self):
        print("---------------Your Cart---------------")
        if len(self.cart)==0:
            print("Your cart is empty")
            return
        total_price=0
        print("Items\t\t\tQunatity")
        print("-----\t\t\t--------")
        for i,j in self.cart.items():
            print(f"{i}:\t\t\t{j}")
            total_price+=(self.products[i]*j)
        print("Total Price :\t\t",total_price)
    
    def payment(self):
        print("Your payment is successful")
        print("Thank you for Shopping")
        self.cart.clear()

cart=Cart()
cart.add_items("Shirt")
cart.add_items("Pant")
cart.add_items("Shoe")
cart.update_items("Shirt",3)
cart.update_items("Pant",5)
cart.update_items("Shoe",2)
cart.view_cart()
cart.payment()
cart.view_cart()
cart.add_items("T-shirt")
cart.add_items("Shirt")
cart.add_items("Pant")
cart.view_cart()