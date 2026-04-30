#  1: create the dic 
thisdict={
    "brand" : "BMW",
    "model" : "X5",
    "year" : 2020,
}
print(thisdict)

# 2: change item in the dictionary
# thisdict["year"] = 2021
# print(thisdict)

# 3: change the values
# x = cars.values()
# print (x)
# cars["year"] = "30494"  
# print(x) 

# 4: change the item
# x = cars.items()
# print (x)
# cars["year"] = "30494"  
# print(x) 

# update the dictionary
thisdict.update({"color": "red"})
thisdict.update({"model": "X6"})
print(thisdict)