# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# txt = "We are the so-called "Vikings" from the north."
# to fix this problem use \
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# escape character

# \'	Single Quote	
txt = 'It\'s alright.'
print(txt) 

# \\	Backslash	
txt = "This will insert one \\ (backslash)."
print(txt) 

# \n	New Line
txt = "this is usefull\n for you only"	
print(txt)

# \r	Carriage Return	
txt = "Hello\rWorld!"
print(txt) 

# \t	Tab
txt = "Hello\tWorld!"
print(txt)
# \b	Backspace
txt = "Hello\bWorld!"
print(txt)

# \ooo	Octal value
txt = "\110\145\154\154\157"
print(txt)	

# \xhh	Hex value 
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
