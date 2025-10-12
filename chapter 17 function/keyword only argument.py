# to specify that a function can have keyword argumenr , add *, before the argumrnt
def  function (*, x):
    print (x)
function (x=3)

# without the * you are allowed to use postional argument 
def function (x):
    print(x)
function (3)

# but with this you cannotuse postional argumrnt you get an error
def function (*, x):
    print(x)
function(3)