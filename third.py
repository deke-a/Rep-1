def area_rectangle(l, b):
    print ("Square of Rectangle = ", square)

x = { "one" : [2,4], "two" : [6,4], "three" : [7,3], "four" : [5,1], "five" : [0,7]} 
list = []

for variable in x:
    l = x[variable][0]
    b = x[variable][1]
    square = l * b
    print ("Square of Rectangle = ", square)
    list.append(square)
    
print ("All Squares = ", list)