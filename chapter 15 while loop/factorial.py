#  Using a while loop to find the factorial of a number

num = 5  # You can change this to any number
factorial = 1
count = 1

while count <= 5:
    factorial = factorial * count
    count = count + 1
print(f"The factorial of {5} is: {factorial}")

# Output: The factorial of 5 is: 120
