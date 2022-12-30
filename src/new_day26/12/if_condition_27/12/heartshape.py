
for i in range(1, 6):
    for x in range(i, 6):
        print(" ", end=" ")
    for y in range(2, i-2):
        print("*", end="   ")
    print(" ")
for i in range(1, 6):
    for x in range(1, i):
        print(" ", end=" ")
    for y in range(i, 6):
        print("*", end="   ")
    print(" ")
