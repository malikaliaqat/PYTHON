# A lambdha function is smaal anonymous function
# A lambdha function can take any number as a argument but only one expression
# Syntax
# lambda argument : expression

# example 
''' remeber lambda can take many number as an argument'''
# Add 10 to argumrnt a , return result
# x = lambda a : a+10
# print(x(5))

# x = lambda a, b : a*b 
# print ( x (5,6))

# x = lambda a, b , c : a*b*c
# print(x (3,4,5,))

# x = lambda a,b,c,d,e,f : a*b*c*d*e*f
# print(x(4,5,6,7,8,9,))



def double (x):
  return x * 2
print (double(5))
#  with lambda 

double = lambda x : x*2 
print(double(5))

#  if i dont use lambda this code will be like 
# def x (a,b ):
#   return a - b 
# print (x(4,3))