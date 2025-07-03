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

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#  function return boolean value
def myFunction() :
  return True
print(myFunction())    # output = true

def myFunction():
  return False
print (myFunction())    # output = false


def myfunction():
 return True
if myfunction():
  print("yes")
else:
  print("no")

#   Check if an object is an integer or not:
x = 200
print(isinstance(x, float))

