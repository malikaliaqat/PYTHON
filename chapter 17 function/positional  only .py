# Add ,/ after argument to specify that the function only have positional argumrnt
# 1:
def function (x,/):
    print (x)
function(3)

# 2
def function (x):
    print(x)
function (x=3)

# 3:
def function (x, /):
 print(x)
function (x = 3)
# But when adding the , / you will get an error if you try to send a keyword argument