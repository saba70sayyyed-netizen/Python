class product:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category


    def show_details(self):
        print("product name:",self.name)
        print("Product price:",self.price)
        print("Product category:",self.category)


class electronics_product(product):
    def warranty(self):
        print("warranty: 1 year")
   
    #object1
product1=product("Shoes",15000,"Fashion")

product2=electronics_product("Laptop",45000,"Electronic")

product1.show_details()
print()
product2.show_details()
product2.warranty()

##################################################################

class person:
    def __init__(self,name,age,education,gender):
        self.name=name
        self.age=age
        self.education=education
        self.gender=gender
    
    
    def show_details(self):
        print("\n ***Basic Details***")
        print("Name=",self.name)
        print("Age=",self.age)
        print("Education=",self.education)
        print("Gender=",self.gender)

class working_person(person):
    def __init__(self,name,age,eductaion,gender,income,company):
        super().__init__(name,age,education,gender)
        self.income=income
        self.company=company


    def show_work_details(self):
        print("\n ***Work Details***")
        print("Income=",self.income)
        print("Company=",self.company)
        
name=input("Enter person Name")
age=int(input("Enter person age"))
education=input("Enter person qualification")
gender=input("Enter your gender")
income=int(input("Enter person income"))
company=input("Enter person company name")


marriage=input("Are you married ? Yes/No")
if marriage=="y":
    w=input("Enter Husband Name")
else:
    w="Not Married"


house=input("Do you have your own house ? Y/N")
person1=working_person(name,age,education,gender,income,company)
person1.show_details()
person1.show_work_details()


print("\n ***Family details***")
print("Married",marriage)


if marriage=="y":
    print("Husband Name=",w)
    

print("Own house=",house)
