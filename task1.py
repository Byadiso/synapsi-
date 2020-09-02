#task 1


products = [
    {"name": "Prod1", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod2", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod3", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod4", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod5", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod6", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod7", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod8", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod9", "amount": {"min": 10000, "max": 99999}, "price": {"min": 0, "max": 100}},
    {"name": "Prod10", "amount": {"min": 10000, "max": 99999}, "price": {"min": 0, "max": 100}},
]
obj_list = []


class ParentProduct:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name of this product is" + {self.name})



# code for  product class


class Product(ParentProduct):
    def __init__(self,name , amount, price):
        ParentProduct.__init__(self,name)
        self.price = price
        self.amount = amount
        # self.name = name

    def show_price(self, currency):
        print(str(self.name) + " price is " + str(self.price) + str(currency) )
    
    def show_amount(self):
            print(str(self.name) + ' amount is ' + str(self.amount)) 


    def calculate_total_value(self):
        return  print(self.amount * self.price) 

       
    
# I was able to use my methods with my  class created in  examples of product1 = Product("avocado", 4, 200)

product1 = Product("avocado", 4, 200)
product1.show_price(" $ ")
product1.show_amount()
product1.calculate_total_value()
    
obj_list.append(products)

for product in obj_list:
    print(product)


# my logic was limited only here   
