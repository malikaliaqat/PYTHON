# write A python code to print content of directoy using os module.search online for the function which does that


import os

path = '/path/to/your/directory'

entries = os.listdir(path)

for name in entries:
    print(name)