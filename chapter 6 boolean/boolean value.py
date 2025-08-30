#  In programing language we often need to know the if the expression is ture or false
a = 3
b = 4
if a < b:
 print("a is less than b")
else:
 print("a is not less than b")

# Evaluate Values and Variables
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# these value are true
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#  some value are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})




def myfunction():
 return True
if myfunction():
  print("yes")
else:
  print("no")

#   Check if an object is an integer or not:
x = 200
print(isinstance(x, float))

