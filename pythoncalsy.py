def addition(a,b):
    return a+b
def subtraction (a,b):
    return a-b
def multiplication (a,b):
    return a*b
def division(a,b):
    if b==0:
        return "Cannot divide by 0 "
    return a/b
     
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
operation=int(input("Enter the number of the operation you want to perform:")) 
try:
 if operation in range(1,5):
    
    a=int(input("Enter the first number:")) 
    b=int(input("Enter the second number:"))

 if operation==1:
     print(addition(a,b))
 if operation==2:
     print(subtraction(a,b))
 if operation==3:
     print(multiplication(a,b))
 if operation==4:
     print(division(a,b))
 else:
    print("Invalid operation number selected!")
except ValueError: 
    print("Invalid input enter valid numbers")