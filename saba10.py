try:
    a=10
    b=0
    c=(a/b)
    print(c)
except:    
    print("Error found")

##################################

try:
    num=int(input("Enter a number:"))
    print("Number is:",num)
except ValueError:
    print("Please enter a valid number")


#################################################

try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print(a/b)
except ValueError:
    print("Please enter a valid number")
except ZeroError:
    print("Cannot divide by zero")

######################################################

try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print(a/b)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

#######################################################

file=open("saba file handling.txt","w")
file.write("Saba")
file.close()

########################################################

file=open("SABA FILE.txt","w")
file.write("hello! I'm Saba")
file.write("\nI'm from Mumbai")
file.close()

#########################################################

file=open("Saba Day11.txt","r")
content=file.read()
print(content)
file.close()
