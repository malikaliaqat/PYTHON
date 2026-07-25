# # # '''Global variable are like variable that are create outside the  function 
# # # they can be accessed from any where in the program
# # # we make global variable because we want to use the variable in the function
# # # if you want to change a global variable inside a function.'''

# x = "awesome"        # Global variable
# def myfunc():
#    print("Python is " + x)  # Accesses the global variable x
# myfunc()           # Function call 
# #   Output: Python is awesome

# x  = "GORGEOUS"
# print("malika is " + x)   
# #  Output: malika is gorgeous

# x= "amazing"
# def myfunc():
#   print ("malike is " + x)
# myfunc()

# #   If you use the global keyword, the variable belongs to the global scope:
# #  ''' so there is why dont we write the myfunc at the end of the code because it will run in infinite loop. 
# #   In the previous question we first give the variable then we call the function
# #   But in this question  call the function before the variable so that why we have to write the myfunc brfore the print'''
# x = "poor"
def myfunc():
  global x
  x = "amazing"
myfunc()
print("malika is " + x)

# #  To change the value of a global variable inside a function
# #  In this question its print x is fantatis because   i use the global which change the global vriable to x
# x = " amazaing"
# def myfunc():
#   global x
#   x = "fantatis"
# myfunc()
# print (" malika is " + x)

# #  In this question its print x is awesome because   i  dont use the global varibale and x is local variable inside the function
# x = 'awesome'
# def myfunc():
#   x = 'fantastic'
# myfunc()
# print('Python is ' + x)


