#  create tuple
thistuple = ( " apple ", "banana " ,"cherry ","date")
print(thistuple)

#  access tuple item
thistuple[0]  # Output: apple
thistuple[1]  # Output: banana
thistuple[2]  # Output: cherry
thistuple[3]  # Output: date


#  access tuple item using negative
thistuple[-1]  # Output: date
thistuple[-2]  # Output: cherry
thistuple[-3]  # Output: banana

# access tuple item using range
thistuple[0:1] # Output: ('apple',)
thistuple[1:3]  # Output: ('banana', 'cherry')
thistuple[2:3]  # Output: ('cherry',)

# access tuple item using range with negative index
thistuple[-2:]  # Output: ('cherry', 'date')
thistuple[-3:-1]  # Output: ('banana', 'cherry')
