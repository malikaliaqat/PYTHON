# Example 4: Using a while loop to find the largest number in a list

list = [2,7,9,4,6,8]
largest = list[0]
count = 1
while count < len(list):
    if list[count] > largest:
        largest = list[count]
        count += 1
print("The largest number in the list is:", largest)