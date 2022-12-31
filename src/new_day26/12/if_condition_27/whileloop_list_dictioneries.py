un_veri = ['amol', 'atul', 'atharv', 'girish']
verified = []
while un_veri:
    i = un_veri.pop()
    print("verifying user :"+i.upper())
    verified.append(i)
print("\n the following user get confirmed: ")
for confirmed_user in verified:
    print(confirmed_user.upper())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


