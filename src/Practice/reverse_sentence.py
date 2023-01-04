#.. reversing full sentense

x = input("Please enter the sentence:-\n")
word = x.split(" ")

reverse = []
while word != []:
    i = word.pop()
    reverse.append(i)

ans = " ".join(reverse)
print(ans)


