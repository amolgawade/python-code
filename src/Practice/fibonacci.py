num = int(input("Enter the  number"))

x = 0
print(x, end=" ")
y = 1
print(y, end=" ")
z = x + y
print(z, end=" ")
while (y + z) < num:
    x = y
    y = z
    z = x + y
    print(z, end=" ")
