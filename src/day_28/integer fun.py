f_name = "amol"
l_name = "gawade"
age = "27"

b = 13+20+10
full_name = f_name+l_name

print(full_name+age + str(b))

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'm - 80'
print(motorcycles)
x = motorcycles.pop()
print(x)
print(motorcycles)

square = [value**2 for value in range(1, 11)]
print(square)
if "80" in square:
    print("hi")

i = 64
if i in square:
    print("yes")
else:
    print("no")

m = input("give value :- ")
if m in square:
    print("yes")
else:
    print("no")


square = [value**2 for value in range(1, 11)]

if 16 in square:
    print("yes present....")
if 36 in square:
    print("yes i m here")
