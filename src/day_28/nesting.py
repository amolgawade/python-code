aliens = []

for alien in range(20):
    new_alien = {'color': 'green', 'size': 'medium', 'point': '5'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print("total no of alien :- "+ str(len(aliens)))

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['size'] = 'big'
        alien['point'] = '10'

for alien in aliens[:5]:
    print(alien)
print("...")





