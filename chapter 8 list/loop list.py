
# # 1: create list
thislist = ["apple", "banana", "cherry"]
print(thislist)

# # 2: loop use
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# 3: using range
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


# # 4: using while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

# # 5: using list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

