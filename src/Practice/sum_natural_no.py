#.. to find natural no

print("To find the sum of natural no start from 1 to n ")
num = int(input("enter the value n : "))
if num < 0:
    print("please enter the valid no")
elif num > 0:
    i = (num*(num+1))/2
    print("sum of natural "+str(num)+" is =  "+str(i))
else:
    print(" ")
