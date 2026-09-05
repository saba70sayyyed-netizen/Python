print("<<-----Welcome to Canara Bank----->>")
print("Please insert your card")
AccNum=input("Please Enter your account Number---")
Pin=""
UsrInputPin=""
Balance=0
Option=0
WithDrawAmount=0

if AccNum=="10190":
    print("*Welcome Saba*")
    pin="7208"
    Balance=190000
    for attemp in range(3):
        UsrInputPin=input("Please Enter your pin:")
        if UsrInputPin==pin:
            while True:
                print("Please select an option")
                print("1.Check balance")
                print("2.Withdraw money")
                print("3.Deposit money")
                print("Exit")
                Option=int(input("Your Option:"))
                if Option==1:
                    print("Your balance is:",str(Balance))
                elif Option==2:
                    WithDrawAmount=int(input("Enter the Amount you want to withdraw:"))
                    Balance=Balance-WithDrawAmount
                    print("Your new balance is:"+str(Balance))
                    print("Please collect rupees"+str(WithDrawAmount))
                elif Option==3:
                    CreditAmount=int(input("Enter the amount you want to credit"))
                    Balance=Balance+CreditAmount
                    print("Your new balance is:"+str(Balance))
                    print("Please deposite rupees"+str(CreditAmount))
                else:    
                    break
                   
        else:
            print("Wrong PIN")
            if attemp==2:
                print("Wrong PIN entered 3 times.your card has been blocked.")
else:
    print("Invalid Account number please contact the bank.")
            
          
