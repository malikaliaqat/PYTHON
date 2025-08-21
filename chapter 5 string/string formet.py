# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# age = 36
# txt = "My name is John, I am " + age
# print(txt)

# so to concate this we use the formet string
age = 67
txt= f"my name is malika liaqat , i am {age}"
print(txt)

#  placeholder (A placeholder can contain variables, operations, functions, and modifiers to format the value.)
price = 59
txt = f"The price is {price} dollars"
print(txt)

#  placehodler contain modifer
# modifer (a modifer include colon:snf follow by legal formet type like .2f which means fixed point number with 2 decimals:)
prince = 67
txt =f"the price is {price:.2f} dollar"
print(txt)

# placeholder can do the math operation
txt = f"the price is {2*3}"
print(txt)
txt = f"the price is {2-3}"
print(txt)
txt = f"the price is {2/3}"
print(txt)
txt = f"the price is {2+3}"
print(txt)
