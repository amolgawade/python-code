cake = {'flav': 'apple',
         'colors': ['green', 'red', 'redish-yellow']}

print("you ordered the  "+cake['flav']+" -cake. which have following color")

for color in cake['colors']:
    print(color)

height = input("how old are you")
print(int(height))

def describe_pet(animal_type,name):
    print("\n I have "+animal_type+".")
    print("The name of my "+animal_type+" is ; "+name)

describe_pet('cat','ninavi')

def desc_pet(name, animal_type='dog'):
    print("\n I have "+animal_type+".")
    print("The name of my "+animal_type+" is ; "+name)

desc_pet(name='tukya')
desc_pet('tomy')

