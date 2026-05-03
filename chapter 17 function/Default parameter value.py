# if we call without passing any argument it will take the default values
def function ( country = "pakistan" ):
    print(" i am from " + country )

function ( " imdia ")
function ("japan")
function ("china")
function()

#  passing list as an arrgument 

# 1:
def function(list = [1,2,3,4,5]):
    for i in list:
        print(i)
function([1,2,3,4,5])
function([6,7,8,9,10])

# 2: 
def function(food):
    for x in food:
        print (x)

function(["pizza", "burger", "pasta"])


# 3:
def function ( food ):
    for x in food :
        print(x)
    
fruit = ["apple", "banana", "mango "]

function(fruit)