# 1:  create tuple
x = ("apple", "banana", "cherry", "date")
print(x)
#  Output: ('apple', 'banana', 'cherry', 'date')


#  2: change item in tuple
x = ("apple", "banana", "cherry", "date")
y = list(x)
y[2] = "kiwi"
x = tuple(y)
print(x)
# Output: ('apple', 'banana', 'kiwi', 'date')

# this code by user
x = ("apple", "banana", "cherry", "date")
y = list(x)
n = int(input("Enter the index of the item you want to change: "))
y[n] = "kiwi"
x = tuple(y)
print(x)


# 3: change item with negative index
x = ("apple", "banana", "cherry", "date")
y = list(x)
y[-2] = "kiwi"
x = tuple(y)
print(x)
# Output: ('apple', 'kiwi', 'cherry', 'date')


#  4: change item with range
x = ("apple", "banana", "cherry", "date")
y = list(x)
y[1:3] = ["pear","peach"]
x = tuple(y)
print(x)


# 5: change item with range and negative index
x = ("apple", "banana", "cherry", "date")
y = list(x)
y[-2:-3] = ["pear","peach"]
x = tuple(y)
print(x)
# Output: ('apple', 'banana', 'cherry', 'date') - no change since range is invalid
