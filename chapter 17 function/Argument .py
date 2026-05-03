
# ******************************Arguments***********************
# Arguments are specified after the function name. inside the parenthese . you can add many argument as you want

# 1:

# def my_function (fname):
#     print (fname)
# my_function("malika")
# my_function("dua")
# my_function("soha")

# # 2:

# def average (a, b):
#     print (" The average of two number is :", (a+b/2))

# average(4,6)

# ***********************************Tyes of argument******************************
# Default argument 
# keyword argument
# arbitary argument
# required argument
# variable lenght argument
# positional argument
# ********************************Default Argument****************
# We can provide a default value while creating a function . 
# This way the function assume a default  value even if a value is not provided in then function call for that argument 
#  for example :

# 1:
def function( a=3 , b=4):
    print ("The avaerage is :", (a+b/2))

function(b = 3, a = 8)
# #  it take the b defaut vallue 4 from upper function if never give the value of b in the function call

# # 2:
# def function ( fname , mname ="liaqat", lname = " ali "):
#     print ("hello, , My name is "+ fname,mname,lname)

# function("malika", mname= "ali")

# # ************************************************keyword Argument**********************************************
# # In this we prvide the argument with the key = value syntax , this the way the interpreter recognise the argument by the parameter name.
# def name (fname , mname , lname ):
#     print("my name is "+ fname , mname , lname )

# name (fname = "malika ",mname="liqat", lname= "ali") 

#  see in this we  do not need to follow the order of the parameter in the function definition we can give any order in the function call
#  like this:
# def average (a = 7 , b = 8 ):
#     print ("The average is : ", (a+b/2))

# average(b= 10 , a= 5)
#  in this we pass the b argument first then a but in the default function  we care about the order


