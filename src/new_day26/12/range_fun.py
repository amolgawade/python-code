square = []
for x in range(1, 10):
    value = x**2
    square.append(value)

print(square)


x = [1, 2, 3, 4]
y = [5, 6, 7, 8, 9]
x.append(y)
print(x)

x = [value**2 for value in range(10, 21)]
print(x)

age_0 = 20
age_1 = 30
if age_0 > 15 or age_1 >= 35:
    print("\nTrue")
else:
    print("\nfalse")


for x in range(1, 100):
    if x == 50:
        print("\ntrue")

x = list(range(31))
print(x)
for i in x:
    if i >= 10:








