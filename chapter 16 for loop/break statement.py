
#  break statement
# fruits = ["apple", "banana", "cherry", "orange"]
# for x in fruits:
#   print(x)
#   if x == "cherry":
#     break
  

#   Exit the loop when x is "banana", but this time the break comes before the print:

# fruits = ["apple", "banana", "cherry", "orange"]
# for x in fruits:
#   if x == "cherry":
#     break
#   print(x)

#    for not print any word
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

#  break statement in a for loop
# for x in range(6):
#   if x == 2:
#     break
#   print(x)


#  print before the breake statement
# for x in range(6):
#   print(x)
#   if x == 2:
#     break

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")