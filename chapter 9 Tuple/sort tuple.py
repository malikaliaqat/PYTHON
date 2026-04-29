#  1:create tupple
thistuple = ["orange", "mango", "kiwi", "pineapple", "banana"]
thistuple.sort()
print(thistuple)

# 2: decresing
thistuple.sort(reverse= True)
print(thistuple)
# Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#3: using sort to case insentive
thistuple = ["banana", "Orange", "kiwi", "Pineapple", "apple"]
thistuple.sort(key=str.lower)
print(thistuple)

#  4: reverse the tuple by sort 
thistuple = ["banana", "kiwi", "orange", "pineapple", "apple"]
thistuple.reverse()
print(thistuple)