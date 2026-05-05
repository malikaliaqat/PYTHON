# write a program to mine a log file and find out ehrther it contain python
with open ("log.txt") as f:
  c = f.read()
if "python" in c :
  print("python is present in the file")
else :
  print("pythhon is not present in the file")