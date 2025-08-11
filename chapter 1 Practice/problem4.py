# label the program wriiten in proble 3
import os

# specify the directory you want to inspect
path = '/'  # e.g. '/home/user/documents' or r'C:\Users\User\Documents'

# get a list of files and folders in that directory
entries = os.listdir(path)

# print each entry
print (entries)