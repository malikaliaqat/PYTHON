# calculator python
operator=input("(+,-,*,/)")
a=float(input("enter the first number"))
b=float(input("enter the first number"))
if(operator=="+"):
    print(a+b)
elif(operator=="-"):
    print(a-b)
elif(operator=="*"):
    print(a*b)
else:
    print(a/b)



# ************************************************calculator*******************************************
num1 = float(input("Enter first number: "))
num2 = float(input("enter second number:"))
print(
    "Enter 1 for the addition \n Enter 2 for the substraction \n Enter 3 for the multiplication \n  Enter 4 for the dividion "
)
operator = input("Enter your choice from 1 to 4 =")
if operator =="1":
    print("The additin of two number is ", num1+num2)
elif operator=="2":
    print("The substraction of two number is ", num1-num2)
elif operator=="3":
    print("The multiplication of two number is ", num1*num2)
elif operator == "4":
    if num2 != 0:
        print("The division of two numbers is", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("invalid numeber")