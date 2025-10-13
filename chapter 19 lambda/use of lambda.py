# why ise of lambda 
#  because lambdais better shon when you use then as anonymous function inside another function
def function(n):
   return lambda a : a * n
m = function(5)
n = function(6)
print(m(6))
print(n(4))