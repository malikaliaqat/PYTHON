# 1: create tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)


# 2: add item to tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y = ("orange",)
thistuple += y
print(thistuple)
# Output: ('apple', 'banana', 'cherry', 'orange')


