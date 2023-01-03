'#finding max/min number among three number'

x = int(input("Enter the first number"))
y = int(input("Enter the second number"))
z = int(input("Enter the third number"))

if x > y and x > z:
    if y > z:
        print(str(x)+">"+str(y)+">"+str(z))
    else:
        print(str(x)+">"+str(z)+">"+str(y))
    print(str(x)+" is greater among them")
if x < y and y > z:
    if x > z:
        print(str(y)+">"+str(x)+">"+str(z))
    else:
        print(str(y)+">"+str(z)+">"+str(x))
    print(str(y)+" is greater among them")
if z > y and x < z:
    if x > y:
        print(str(z)+">"+str(x)+">"+str(y))
    else:
        print(str(z)+">"+str(y)+">"+str(x))
    print(str(z)+" is greater among them")