
#  1: create list
list = ["apple ,banana", "cherry", "date"]
print(list)
#  output: ["apple ,banana", "cherry", "date"]


# 2:  access list item
print(list[0])  # Output: apple ,banana
print(list[1])  # Output: cherry
print(list[2])  # Output: date\


# 3: access list item using negative index
print(list[-1])  # Output: date
print(list[-2])  # Output: cherry


#  4: access list item using range
print(list[0:2])  # Output: ['apple ,banana', 'cherry']
print (list[2:4]) # Output: ['date']


#  5:  access list item using range with negative index
print(list[-2:])  # Output: ['cherry', 'date']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])  # Output: ['orange', 'kiwi', 'melon']
print(thislist[-5:-2])  

