# # 1: create list
thistuple = ["apple ,banana", "cherry", "date"]
print(thistuple)

# # 2: remove item from tuple
thistuple = ["apple", "banana", "cherry", "date"]
y = list(thistuple)
y.remove("banana")
thistuple = tuple(y)
print(thistuple)

# #  by using user
y = list(thistuple)
n = (input("Enter the index of the item you want to remove: "))
y.remove(n)
thistuple = tuple(y)
print(thistuple)


#  3: remove item from tuple using pop
y = list(thistuple)
y.pop()
thistuple = tuple(y)
print(thistuple)

# delete item from tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)