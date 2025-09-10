# 1: create list
list = ["apple ,banana", "cherry", "date"]
print(list)

#  2: Remove list item
list.remove("cherry")
list.remove("date")
print(list)  # Output: ['apple ,banana']

# 3 : pop the item
list = ["apple ,banana", "cherry", "date"]
list.pop()
print(list)

# 4 : del the item
list = ["apple ,banana", "cherry"]
del list[1]
print(list)

# 5: clear the list
list = ["apple ,banana", "cherry"]
list.clear()
print(list)  # Output: []