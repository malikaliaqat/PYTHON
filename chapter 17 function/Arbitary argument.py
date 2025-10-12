
# **************************Arbitary Arguments**********************
# if you do not know how many argument that will passed into function, add a* before the paremeter name

# 1:

def my_function(*name):
 print(" the name of kids is " )
 for kid in name:
  print(kid)
my_function("malika", "dua", "soha")

# 2:

def my_function(fname):
 print(fname)
my_function("malika")

# 3:

def my_function(*fname):
  for n in fname:
    print (n)
my_function("malika","soha","dua")
    

# 4:

def function(subject, time):
    if time > 0:
        print(subject)
        function(subject, time - 1)  # recursive call only if time > 0

function("math", 3)
    
# 5:
def my_function(*name):
 print(" the name of kids is " + str(len(name)))

my_function("malika", "dua", "soha")