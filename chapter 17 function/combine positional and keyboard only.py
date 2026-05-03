# you can combine the two argument types in a same function
# any argument before the ,/ is positional only and any argument after the * is keyword only
def function(a, b, /, *, c, d):
    print(a+b+c+d)
function( 5,  5 , c = 6, d = 7)