# 1: create dictionary with keys as file names and values as their content
thisdict={
    "brand" : "BMW",
    "model" : "X5",
    "year" : 2020
}
print(thisdict)
# Output: {'brand': 'BMW', 'model': 'X5', 'year': 2020}

# 2: pop 
# thisdict.pop("year")
# print(thisdict)
# Output: {'brand': 'BMW', 'model': 'X5'}

#  3: remove 
del thisdict["model"]
print(thisdict)

#  4: clear
thisdict.clear()
print(thisdict)