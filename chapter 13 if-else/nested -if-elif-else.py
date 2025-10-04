
# ***********************************************nested - if-elif-else******************************************************

# 1:
marks = 85
if marks >= 60:
    print("You passed.")
    
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("You failed.")

# 2:
age = 21
if age >= 18:
    print("You are an adult.")
    if age >= 21:
        print("You can drink alcohol BUT LOW.")
    elif age>=26:
        print("you can drink alcohol")
else:
    print("You are a minor.")


# 3:
age = int(input("Enter the Number : "))
# age = -1
if age < 0:
    print("age is negative")
elif age >= 18:
    print("You are an adult.")
    if age >= 21:
        print("You can drink alcohol BUT LOW.")
    elif age>=26:
        print("you can drink alcohol")
else:
    print("You are a minor.")
    

# 4:
num = int(input("Enter the Number : "))
# num = 17
if num < 0:
    print ("number is negative")
elif num > 0:
    if num <=10:
        print("number is between 1 to 10")
    elif num>10 and num <=20:
        print ("number is between 11-20")
    else :
        print("number is greater than 20")
else:
    print("number is zero")

