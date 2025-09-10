# 1:  create list
list = ["apple ,banana", "cherry", "date"]
print(list)
#   output: ["apple ,banana", "cherry", "date"]

# 2: add list item
list.append("orange")
print(list)  # Output: ['kiwi', 'cherry', 'date', 'orange']

# 3: insert the item at specific position
list.insert(2, "melon")
print(list)  
# Output: ['kiwi', 'cherry', 'melon', 'date', 'orange']

# 4: expend the item means add the multipple itme or list
list1 = ["mango", " banana", "peach"]
list2 = [ "orange", "kiwi"]
list1.expend(list2)
print(list1)  # Output: ['mango', ' banana', 'peach', 'orange', 'kiwi']