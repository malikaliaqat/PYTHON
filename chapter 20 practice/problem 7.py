# write thhe program to find out the line number where python is present from ques 6
# write a program to mine a log file and find out ehrther it contain python

with open ("log.txt") as f:
  lines= f.readlines()

  lineno = 1
for line in lines:
    if "python" in line :
        print(f"python is present in the file . line no :{lineno}")
        break
    lineno = lineno + 1

else :
  print("pythhon is not present in the file")