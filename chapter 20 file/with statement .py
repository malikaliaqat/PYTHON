f = open("file.txt")
print(f.read())
f.close()

# the same can be written usingstatement like this
with open ("file.txt")as f:
   print(f.read())
  
 # you dont have to close the file, it will be closed automactically 
