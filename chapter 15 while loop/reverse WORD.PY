# Example 6: Using a while loop to reverse a string

string = "hello world"
reverse = ""
i = len(string) - 1

while i >= 0:
    reverse = reverse + string[i]
    i = i - 1
print("Reversed word is:", reverse)