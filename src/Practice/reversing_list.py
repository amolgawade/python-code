'#to reversr the given list '

animal = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Panda"]
print(animal)
animal.reverse()
print(animal)
print("\n")

animal_1 = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Panda"]
print("\nTHe original list is :-"+str(animal_1))
animal_2 = []
while animal_1 != []:
    i = animal_1.pop()
    animal_2.append(i)
print("\n here is my reversed list :-"+str(animal_2))

