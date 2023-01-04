# ... verifying the word is palindrome or not

name = input("enter the word :- \n")
rev = ""
for i in name:
    rev = i + rev
print(rev)
if i == rev:
    print(" This word is palindrome")
else:
    print(" This word is not palindrome")
