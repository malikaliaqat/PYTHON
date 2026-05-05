# write a program to read the text from a given file 'poem.txt 'and find out whether it contain the word 'twinkele'
with open ("poem.txt") as f:
    content = f.read()
    if "twinkle" in content:
        print("yes")
    else:
        print("no")