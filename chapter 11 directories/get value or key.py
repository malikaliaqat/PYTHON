# 1: create dictionary with keys as file names and values as their content
thisdict={
    "brand" : "BMW",
    "model" : "X5",
    "year" : 2020
}
print(thisdict)


# 2: to get value specific
x = thisdict.get("model")
print(x)
 # Output: X5


#  3: to get key 
x = thisdict.keys()
print(x)
# Output: dict_keys(['brand', 'model', 'year'])

#  4: to get all values
x  = thisdict.values()
print(x)
# Output: dict_values(['BMW', 'X5', 2020])

# get item
x = thisdict.items()
print(x)
# Output: dict_items([('brand', 'BMW'), ('model', 'X5'), ('year', 2020)])