# recursion is the function which call itself
# def factorial (n):
#   if ( n==1 or n==0):
#     return 1
#   return n * factorial(n-1)
# n = int(input("Enter the number:"))
# print(factorial(n))

# write a program using fucntuon to find the greatest of three number
# def greater(a,b,c):
#   if   a > b and a > c:
#     print("a is greater than b and c :" )
#   elif b > a and b> c :
#     print (" b is greater than a and c")
#   else:
#     print("c is greater than a and b")
# a = int( input("Enter the first number: "))
# b = int( input("Enter the second number: "))
# c = int( input("Enter the third number: "))
# greater(a,b,c)

# write the function to convert the celcius to fahrenheit
# def convert(f): 
#    return 5*(f-32)/9
# f = int(input("Enter the f:"))
# print(convert(f))

# def convert(f): 
#     c = 5 * (f - 32) / 9
#     print(c)  
# convert(10)

# how do you prevent a pythin print function to print a new line at the end
# print("a")
# print("b")
# print("c",end="")
# print("d",end="")

# write a recursive function to sum the first n natural number
# def sum(n):
#   if (n==1):
#     return 1
#   return sum(n-1)+n
# print(sum(4))

# write a function to print first n lines of the following patern 
# ***
# **
# *
# def tree():
#   pass
# n = int(input("enter the number"))
# for i in range(n,0,-1):
#  print("*"*i)

# def pattern(n):
#   # if (n==0):
#   #   return 
#   print("*" * n)
#   pattern(n-1)


# pattern(3)

# write the code the funvtion which convert inches to cms
# def convert(inch):
#    return inch * 2.54
# n = int(input("Enter the number :"))
# print(convert(n))

# write the function to remove a given word from a list strip it at the same time
def rem(l,word):
   n = []
   for item in l:
       if not(item==word):
           n.append(item.strip(word))
   return n

l = ["malika", "harry","dum","ka"]

print(rem(l,"ka"))



#  write a python function to print multiplication table of a given number

def multiply(n):
  for i in range (1, 11):
   print( n*i)
multiply(6)
