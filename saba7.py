a=-5
while a <= 5:
    if a < 0:
        print("Negative Number:",a)
    elif a > 0:
        print("Positive Number:",a)
    else:
        print("Zero",0)
    a += 1

################################################
def hello():
    a=30
    b=7
    print(a+b)
hello()    

################################################
def hello():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print(a+b)
hello()    

###############################################
def hello(a,b):
    result=a+b
    return result
hello(7,80)   

##############################################
def hello(l,b):
    rec_area=l*b
    return rec_area
hello(8,4)    
    
