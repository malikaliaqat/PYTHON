# datatype is the kind of data a value can hold,its tell the computer what kind of operation perform on data
a = 1         # a is the integer
print(a)
b = 23.3      # b is the floating number
print(b)
c = True      # c is boolean vaiable
is_sunny = True
is_raining = False
print(is_sunny)     # Output: True
print(is_raining)   # Output: False
d = "malika"  # d is string
print(d)
e = None      # e is the none tyoe variable
def greet():
    print("Hello")
result = greet()
print(result)  
# Output: None
f = 1j        #d is compleX number
g = ["apple", "banana", "cherry"]   #g is list(use when You need to add/remove/change items)
mylist = [1, 2, 3, 2]
print(mylist[0])
h = "apple", "banana", "cherry"   #h is tuple(use when you want fixed data that doesn’t change)
mytuple = (1, 2, 3, 2)
mytuple[0] = 10
mytuple.append(40) 
i = range(6)	 # i is for range
j = {"name" : "John", "age" : 36}	 # j is dict(A dict lets you store and access data using keys instead of positions (like in lists)
print(j["name"])
k = {"apple", "banana", "cherry"}	 # k i set (use When you need unique values only )
myset = {1, 2, 3, 2}
print(myset)  # Output: {1, 2, 3}
l = frozenset({"apple", "banana", "cherry"}) # l is frozenset (use when you need unique values only and you can’t change 
print(l)
frozenset.add(mango)              #frozeset never add or remove item
n = b"Hello"	# n is bytes	
print(n)
o = bytearray(5)	#o is bytearray	
print(o)
p = memoryview(bytes(5))	#p is memoryview
print(p)

x = str("Hello World")	
print (x)
x = int(20)
print (x)
x = float(20.5)
print (x)
x = complex(1j)
print (x)
x = list(("apple", "banana", "cherry"))
print (x)
x = tuple(("apple", "banana", "cherry"))
print (x)
x = range(6)	
print (x)
x = dict(name="John", age=36)		
print (x)
x = set(("apple", "banana", "cherry"))
print (x)
x = frozenset(("apple", "banana", "cherry"))	
print (x)
x = bool(5)		
print (x)
x = bytes(5)	
print (x)
x = bytearray(5)	
print (x)
x = memoryview(bytes(5))	
print (x)