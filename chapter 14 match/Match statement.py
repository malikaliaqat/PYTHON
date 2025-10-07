# you can use the match statement instead of many if and else statement
# it is more readable and efficient

# syntax
# match expression:
#   case x:
#     code block
#   case y:
#     code block
#   case z:
#     code block

# 1: The match expression is evaluates once
# 2: the value of the expression is matched  value of each case 
# 3: if there is match then it excuted   
#    For exmple

day = 5
match day:
   case 1:
    print("monday")
   case 2:
    print("tuesday")
   case 3:
     print("wednesday")
   case 4:
     print("thrusday")
   case 5:
     print("friday")
   case 6:
     print("saturday")
   case 7:
     print("sunday")

# This is in if-elif-else
day = int(input("Enter the day :  "))
# day = 5
if day < 0:
     print ("nothing")
elif day > 1:
     if day==1:
          print("monday")
     elif day==2:
          print("tuesday")
     elif day==3:
          print("wednesday")
     elif day==4:
          print("thruday")
     elif day==5:
          print("friday")
     elif day==5:
          print("saturday")
     elif day==6:
          print("sunday")
else:
     print(" you enter wrong")

#  combine value in match
day = 4
match day:
    case 1|2|3|4|5:
        print (" today is week day")
    case 6|7:
        print("i love weekend ")

# if statement is guard
month = 4
day = 4
match day:
    case 1|2|3|4|5  if month ==4:
        print("A weekday in a april")
    case 1|2|3|4|5 if month == 5:
        print(" A weekday in a may")
    case _:
        print("no match")

# This question according to if else
month = 5
day = 4

if day in (1, 2, 3, 4, 5) and month == 4:
    print("A weekday in April")
elif day in (1, 2, 3, 4, 5) and month == 5:
    print("A weekday in May")
else:
    print("No match")
