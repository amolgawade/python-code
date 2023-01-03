'#to check number is even or odd'

num = float(input("please enter the number :- "))
print(num % 2)
if (num % 2) == 0:
    print("Given no is even")
elif num % 2 != 0:
    print("Given no is odd")
else:
    print("invalid input")