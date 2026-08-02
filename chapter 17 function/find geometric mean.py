def calculategmean(a,b):
    mean= (a*b)**0.5
    print(mean)
a = 31
b = 41
# if a > b :
#     print (" first number is greater than second number")
# else :
#     print("second number is greater than first nuumber")
calculategmean(a,b)
c = 42
d = 5
# if c > d :
#     print (" first number is greater than second number")
# else :
#     print("second number is grater than first nuumber")
# calculategmean(c,d)

# if a & b > c & d :
#     print ( "the answwer of a and b is greater than c and d")
# else :
#     print("c and d is greater than a and b")


# or  
def isgrater(a,b):
    if a > b :
        print (" first number is greater than second number")
    else :
        print("second number is greater than first nuumber")
    return (a*b)**0.5
print(isgrater(a,b))
print(isgrater(c,d))


def issmaller(a,b):
    if a < b :
        print (" first number is smaller than second number")
    else :
        print("second number is smaller than first nuumber")
    return (a*b)**0.5
print(issmaller(a,b))
print(issmaller(c,d))


