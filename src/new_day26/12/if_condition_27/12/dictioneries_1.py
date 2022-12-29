dog_1 = {'color':'green','point': 5}

print(dog_1['color'])
print(dog_1['point'])
new_point = (dog_1['point'])
print("you just earned "+str(new_point)+"  points congrats")

dog_1 = {'color':'green','point': 5}
print(dog_1)
dog_1['x_position'] = 0
dog_1['y_position'] = 25
print(dog_1)
dog_1['color'] = 'blue'
print("the new color of dog_1 is "+dog_1['color']+' .')
print(dog_1)

dog_1 = {'color': 'green', 'point': 5, 'x_position': 0, 'y_position': 25 , 'speed':'medium'}
print('original x-position '+str(dog_1['x_position']))
if dog_1['speed'] == 'slow':
    x_increment = 1
elif dog_1['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
dog_1['x_position'] = dog_1['x_position'] + x_increment
print('new x-position  '+str(dog_1['x_position']))
print(dog_1)
del dog_1['point']
print(dog_1)

user_0 = {'name':'Amol','email':'amolsg863',"b'day":'aug6/1995','add':'baramati'}
for key , value in user_0.items():
    print('\n '+key+' :'+value)
    print(key.title())


fav_lang = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python' }
print("The following things have been mentioned:")
for name,value in fav_lang.items():
    print(name.title()+":"+value.title())
for lang in set(fav_lang.values()):
    print("\n"+lang.title())

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0,alien_1,alien_2],
for alien in aliens:
    print(alien)

alien = []
for alien_no in range(30):
    new_alien = {'color': 'green', 'size': 'medium', 'speed': 'slow'}
    alien.append(new_alien)
    for ali in alien[:2]:
        print(ali)
    print('....')
    print("Total no of aliens : "+str(len(alien)))


aliens = []
for alien_no in range(20):
    new_alien = {'color': 'green', 'size': 'medium', 'speed': 'slow'}
    aliens.append(new_alien)
for ali in aliens[0:3]:
    if ali['color'] == 'green':
        ali['color'] = 'blue'
        ali['size'] = 'big'
        ali['speed'] = 'fast'
for ali in aliens[0:5]:
    print(aliens)
    print("....")
print("Total no of aliens : "+str(len(aliens)))

gun = {'type': 'shotgun', 'range': '20 m', 'color': ['black', 'grey', 'german-black'], }
print("You order the following gun :"+gun['type']+"\nthey are available in follwing color : ")
for color in gun ['color']:
    print('\t'+ color)

users = {'aeinstein': {'first': 'albert','last': 'einstein','location': 'princeton', },
         'mcurie': {'first': 'marie','last': 'curie','location': 'paris', }, }

for name,user_info in users.items():
    print('\n username : '+ name)
    full_name = user_info['first']+' '+user_info['last']
    Location = user_info ['location']
    print("full name : "+full_name.upper())
    print("location : "+Location.title())

