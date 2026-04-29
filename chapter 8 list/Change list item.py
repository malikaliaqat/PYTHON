# 1: create list
list = ["apple ,banana", "cherry", "date"]
print(list)
#  output: ["apple ,banana", "cherry", "date"]

# 2: change list item
list[0] = "kiwi"
print(list)  # Output: ['kiwi', 'cherry', 'date']
list[1] = "orange"
print(list)  # Output: ['kiwi', 'orange', 'date']

# 3: change list item using range
list [1:3] = ["melon", "mango"]
print(list)  # Output: ['kiwi', 'melon', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# 4 change list item using range with negative index
list[-2:] = ["peach", "plum"]
print(list)  # Output: ['kiwi', 'peach', 'plum']


