#..reversing the given string

x = input("enter the given string/word:\n")
for i in reversed(x):
    print(i, end="")


x = input("\nenter the given string/word:\n")
rev = " "
for i in x:
    rev = i + rev
print(rev)



