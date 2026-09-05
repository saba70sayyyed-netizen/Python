CartTotal=int(input("Enter your total bill--"))
MemberShip=(input("do you have a membership?(y/n)"))
Coupon=(input("do you have a coupon?(y/n)"))
Coupon=""
Toffee=False
Discount=0

if MemberShip=="y":
    age=int(input("Enter your age:"))
    if age>=60:
        discount=0.15*CartTotal
        CartTotal=CartTotal-Discount
        print("You get a senior Citizen member discount of 15%")
    else:
        Discount=0.1*CartTotal
        CartTotal=CartTotal-Discount
        print("You get a discount of 10%")
else:
    print("You are not eligible for membership discount")
if Coupon=="y":
    CouponName=input("Enter your coupon here")
    if CouponName=="WELCOME" or "ANNIVERSARY":
        Discount=0.05*CartTotal
        CartTotal=CartTotal-Discount
        print("You get a coupon discount of 5%")
    else:
        print("Wrong coupon name")
else:
    print("You are not eligible for coupon discount")
KidCheck=(input("Do you have a kid with you?(y/n)"))
if KidCheck=="y":
    Toffee=True
    print("Your cart total is "+str(CartTotal)+"and you get a toffee")
else:
    Toffee=False
    print("Your cart total is"+"str(CartTotal)")

******************************************************************************************************************


