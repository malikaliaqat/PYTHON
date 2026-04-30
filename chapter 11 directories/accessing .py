# 1: create dictionary with keys as file names and values as their content
thisdict={
    "brand" : "BMW",
    "model" : "X5",
    "year" : 2020
}
print(thisdict)
# Output: {'brand': 'BMW', 'model': 'X5', 'year': 2020}

# 2: access dictionary values using keys
print (thisdict["brand"])
 # Output: BMW

# 3: to get value
x = thisdict.get("model")
print(x)
 # Output: X5


#  4: to get key 
x = thisdict.keys()