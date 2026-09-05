#THIS IS MY FIRST PYTHON PROGRAM
Name="Hello,I'm Saba"
Age="I am 20 years old"
Place="I live in Pune"
Colour="Black and Purple"
Print("Name:",Name)
print("Age:",Age)
print("Place:",Place)
print("Colour:",Colour)
print("This is my First program")

**********************************************************************************************************

#GST CALCULATOR
print("Welcome to the GST calculator")
OneItemPrice=int(input("What is your price per one item?"))
NumberOfItems=int(input("How many items do you have?"))
GstPercent=int(input("What is the GST percent?"))
TotalPrice=OneItemPrice*NumberOfItems
GstCost=GstPercent/100*TotalPrice
TotalAmount=TotalPrice+GstCost
print("Total amount to pay=\u20B9"+str(TotalAmount))

************************************************************************************************************

print("<<-----Welcome to Canara Bank----->>")
print("Please insert your card")
AccNum=input("Please Enter your account Number---")
Pin=""
UsrInputPin=""
Balance=0

if AccNum=="10190":
    print("*Welcome Saba*")
    pin="7208"
    Balance=190000
    for attemp in range(3):
        UsrInputPin=input("Please Enter your pin:")
        if UsrInputPin==pin:
            print("PIN Verified")
            print("Your Balance is:\u20B9"+str(Balance))
            break
        else:
            print("Wrong PIN")
            if attemp==2:
                print("Wrong PIN entered 3 times.your card has been blocked.")
else:
    print("Invalid Account number please contact the bank.")
            
          
