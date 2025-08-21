#  string are the text that are written  or sourrounded in the single or double quotes
# like "hello" is same as 'hello'
print("hello")
print('hello')

#  quotes inside quotes
print ("malika is my best 'friend'")
print ('malika is my best "friend"')

# assign string to varaible
a = "hello"
print(a)

# multiline string
a = """ hey there  myself malika liaqat and i'm currently doing my bscs and foucus onpython jo ho nahi kue kay
 i'm interest watching dramas  movies and listing  songs"""
print(a)

a = ''' hey there  myself malika liaqat and i'm currently doing my bscs and foucus onpython jo ho nahi kue kay
 i'm interest watching dramas  movies and listing  songs'''
print(a)

# string as array
a = "hello there"
print(a[1])

#  looping through the string
for x in "hello there":
 print(x)

# lenght if string
a = "hello there"
print(len(a))

# check the string
txt = "The best things in life are free!"
print("free" in txt)
a = " my self malika liaqat and i'm doing bscs"
if "bscs" in a:
 print("yes bscs is present")
 a = " my self malika liaqat and i'm doing bscs"
if "chemistry"  not in a:
 print("not chemitry  is not present")