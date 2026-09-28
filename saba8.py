class product:
    name=""
    price=0
    category=""
    #object1
product1=product()
product1.name="Laptop"
product1.price=45000
product1.category="Electronic"
    #object2
product2=product()
product2.name="Shoes"
product2.price=15000
product2.category="Fashion"
    #product details print
print("Product-1")
print("Name:",product1.name)
print("Price:",product1.price)
print("Category:",product1.category)
print()
print("Product-2")
print("Name:",product2.name)
print("Price:",product2.price)
print("Category:",product2.category)

####################################################

class product:
    name=""
    price=0
    category=""
    #object1
product1=product()
product1.name=input("Enter the product name:  ")
product1.price=int(input("Enter the price of the product:  "))
product1.category=input("Enter the category of the product:  ")
    #object2
print()
product2=product()
product2.name=input("Enter the product name:  ")
product2.price=int(input("Enter the price of the product:  "))
product2.category=input("Enter the category of the product:  ")
    #product details print
print()
print("Product-1")
print("Name:",product1.name)
print("Price:",product1.price)
print("Category:",product1.category)
print()
print("Product-2")
print("Name:",product2.name)
print("Price:",product2.price)
print("Category:",product2.category)
    
