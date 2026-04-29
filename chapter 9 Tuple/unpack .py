# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# Unpacking a tuple means breaking down the tuple into individual variables.

# 1: create tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)


# 2: unpack tuple
thistuple = ("apple", "banana", "cherry")
red,yellow,mehron = thistuple
print (red)  # Output: apple
print (yellow)  # Output: banana
print (mehron)  # Output: cherry

# 3: unpack tuple with asterisk

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green) # Output: apple
print(yellow) # Output: banana
print(red) # Output: ['cherry', 'strawberry', 'raspberry']