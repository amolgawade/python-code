age = 25
for age in range(22, 27):
    if age == 25:
        print('correct age guess')
    else:
        print("not correct age", end ="###")


for age in range(18, 22):
    if age >= 20:
        print("true")
    else:
        print("\t\n\nfalse")

age_0 = 21
age_1 = 22
if (age_0 >= 30) or (age_1 >= 25) :
    print('\n these is true')
else:
    print('\n here is the ans false')


gun = ['shotgun', 'rocket', 'revolver', 'agni1', 'german', 'desi katta', 'brahmose', 'tank']

if 'agni1' in gun:
    print('\n yes present in gun')
else:
    print('\n not present in gun')
if 'desi katta' in gun:
    print('\n kitila ghenar tu?')


gun = ['shotgun', 'rocket', 'revolver', 'agni1', 'german', 'desi katta', 'brahmose', 'tank']

if 'desi katta' in gun:
    print('\n how much')
else:
    print('not available')
if 'tank' in gun:
    print('\n army kade ja ')


gun = ['shotgun', 'rocket', 'revolver', 'agni1', 'german', 'desi katta', 'brahmose', 'tank']
if 'shotgun' in gun:
    print('\n do you want ')


car = 'tata'
print("is car == 'tata'? i predict true")

age = 2
if age < 4 :
    print("\nentry fee is 0 rupee")
elif age < 18:
    print("\nentry fee is 20 rupee")
else:
    print("\nentry fee is 40 rupee")


age = 15
if age < 4:
    price = 0
elif age < 18:
    price = 20
else:
    price = 40
print("\nyour entry fee is " + str(price) + " rupee.")


age = 30
if age < 4:
    price = 0
elif age < 18:
    price = 20
elif age > 65:
    price = 30
else:
    price = 40
print("\nyour entry fee is " + str(price) + " rupee.")



