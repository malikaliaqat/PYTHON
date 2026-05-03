# you also send the argument with the ke = value syntax

def my_function(child1,child2,child3):
    print ("The older chile is : " + child1)

my_function(child1="Ali",child2="Ahmed", child3="Zeeshan")

# ***********************Arbitary keyword argument , **kwargs***********************
def function(**kid):
    print ("the youngest child is : "+kid["tname"])

function(fname= "malika ", lname = "dua" , tname = " soha ", mname = " uswa") 