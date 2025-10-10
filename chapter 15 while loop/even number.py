#  Using while loop to print even numbers
i = 0
while i < 10:
        i= i + 1
        if i % 2 !=0:
            continue;   
        print(i)


#  Number from user to check whatever number is even or odd
i = int(input("Enter a number: "))

while True:
    if i % 2 == 0:
        print(i, "is an even number")
    else:
        print(i, "is an odd number")
    break 