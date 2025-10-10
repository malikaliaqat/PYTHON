# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

#  syntax
# for item in sequence:
    # code block to be executed for each item
    # This block must be indented

#  example :
#  print the fruits in a list

fruits = [ "apple", " banana", "peach", "orange"]
for x  in  fruits:
    print(x)

#     for range 
for x in range(6):
  print(x) 

#   Using the start parameter:

for x in range(2, 6):
  print(x)

# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")
