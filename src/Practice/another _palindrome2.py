
name = str(input("enter the word :- \n"))
n = len(name)
isPalindrome = True
for i in range(0, int(n/2)):
    if name[i] != name[(n-1) - i]:
        isPalindrome = False
        break


if isPalindrome:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
