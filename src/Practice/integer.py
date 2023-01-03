'#to check if number is positive/negetive /zero'

num = int(input("\nplease enter the number :-"))
while True:
    if num > 0:
        print(str(num)+" = The given number is postive")
    elif num < 0:
        print(str(num)+" = The given number is negative")
    else:
        print("number is zero")
    break