# repeate the program for alist of such word to be censored
words = ["donkey ", "bad" , "good","stupid"]

with open ("file.txt") as f:
   content = f.read()

for word in words:
     content= content.replace(word, "+" * len(word))

with open ("file.txt", "w") as  f:
 f.write(content)