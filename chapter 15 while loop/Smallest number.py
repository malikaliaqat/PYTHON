# Using a while loop to find the smallest number in a list

list = [1,3,5,6,7,8,7,9]
smallest = list[0]
count = 1
while count > len(list):
    # if list[count] < smallest:
        smallest = list[count]
        count += 1
print("The smallest number in the list is:", smallest)