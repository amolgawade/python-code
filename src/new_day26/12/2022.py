
cars = ['Tata', 'suzuki', 'hoda', 'mahendra', 'kia', 'toyota', 'jeep', 'safari', 'Bmw', 'mercedes']
cars.sort(reverse=True)
print(cars)

cars = ['Tata', 'suzuki', 'hoda', 'mahendra', 'kia', 'toyota', 'jeep', 'safari', 'Bmw', 'mercedes']
print('\nhere is the original list:')
print(cars)
print("\nHere is sorted list:")
print(sorted(cars))
print('\n\t from these change the code')
cars = ['Tata', 'suzuki', 'hoda', 'mahendra', 'kia', 'toyota', 'jeep', 'safari', 'Bmw', 'mercedes']
print(cars)
cars.reverse()
print(cars)

cars = ['Tata', 'suzuki', 'hoda', 'mahendra', 'kia', 'toyota', 'jeep', 'safari', 'Bmw', 'mercedes']
print(len(cars))

gun = ['shotgun', 'rocket', 'revolwer', 'agni1', 'german', 'desi katta', 'brahmose', 'tank']
print("\n Here is my orignal list of gun:")
print(gun)
print("\n Here are now they are sorted :")
gun.sort()
print(gun)
gun.sort(reverse=True)
print(gun)
gun.reverse()
print(gun)
print(len(gun))
print(gun[-5])

gun = ['shotgun', 'rocket', 'revolver', 'agni1', 'german', 'desi katta', 'brahmose', 'tank']
for txt in gun:
    print(txt.title() + " : This is very dangerous")
    print("The weapon " +txt.upper()+" , i want to use it "+"\n")


print("These are all weapons are not for sale and use "
          "thanks for asking ")

message = 'hello everyone , i m amol gawade'
print(message)

for value in range(1,5):
    print(value)

num = list(range(1,6))
print(num)
num = list(range(3,30,3))
print(num)

squares = []
for value in range(1,11):
    num = value**2
    squares.append(num)
print(squares)

num = list(range(100, 1000, 100))
print(num)
print(min(num))
print(max(num))
print(sum(num))

num = [value**2 for value in range(2, 21)]
print(num)

num = list(range(1, 100000))
print(num)

print(sum(num))

num = []
for num in range (3, 33):
    txt = list [ num*2 ]
    print(txt)

num = list(range(1,6))
txt = list (num*2)
print(txt)
num = list(range(3,30,3))
print(num)

gun = ['shotgun', 'rocket', 'revolver', 'agni1', 'german', 'desi katta', 'brahmose', 'tank']
print("here are three weapon that are dangerous")
for num in gun[0:5]:
    print(num.title())


my = ['toyota','suzuki']
friend = my[:]

print('my favourite car is: ')
my.append('hero')
print(my)
print("\n my friends favourite car is: ")
friend.append('honda')
print(friend)

gun = ['shotgun', 'rocket', 'revolver', 'agni1', 'german', 'desi katta', 'brahmose', 'tank']
for weapon in gun :
    if weapon == 'tank':
        print(weapon.upper())
    else:
        print(weapon.title())

car = 'BMW'
tar = 'and'

