
name = str(input("enter the word :- \n"))
n = len(name)
isPalindrome = True
for i in range(0, int(n/2)):
    if name[i] == name[(n-1) - i]:
        continue
    else:
        isPalindrome = False
        break


if isPalindrome:
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")
