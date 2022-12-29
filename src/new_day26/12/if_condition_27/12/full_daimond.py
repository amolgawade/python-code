
n = 5
for i in range(n):
    for j in range(i, n-1):
        print(" ", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    for j in range(1, i):
        print("*", end=" ")
    print(" ")
for i in range(n):
    for j in range(1, i):
        print("*", end=" ")
    for j in range(1, i+1):
        print(" ", end=" ")
    for j in range(1, i):
        print(" ", end=" ")
    print(" ")