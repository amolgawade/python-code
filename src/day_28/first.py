print('amol')

print("\tamol")

print("amol\ngawade\nbaramati")
print("name=amol gawde\naddress\n\tbaramati\n\tpragtinagr\n\t devkate niwas")

favorite_language = '   python   '
x= favorite_language.rstrip()
print(x)


txt= "  mangoes   "
x= txt.strip()
print ('out of all fruits',x,'is my favourate')

who= "there are two cat's"
print(who)

person_name1="Amol Gawade"
person_name2="Shvaji Gawade"
print(person_name1.upper(),person_name2.title())

famous_person="albert einstine"
famous_Quote= "A person who never made a mistake never tried anything new."
txt=famous_person+'\n\t' +famous_Quote
print("This is most famous line by brillent scientis : ",txt.upper(),"He was the one who invented the "
                                                             "E=mc^2 and made grate revoulation to science ")

A1="Mahatma Gandhi"
Dia1="The greatness of a nation and its moral progress can be judged by the way its animals are treated."
A2="Pandit Neharu"
Dia2="बिना शांति के, सभी सपने टूट जाते हैं और राख में मिल जाते हैं"
A3="Abddul kalam "
Dia3="You have to dream before your dreams can come true"
add=A1+'\n\t'+Dia1+'\n'+A2+'\n\t'+Dia2+'\n'+A3+'\n\t'+Dia3
print("some famous dialouges:", add.title())


print(10+20-(5/10*200/10)+500)

print(0.2*0.2)
age = 23
message = "Happy " + str(age)+'rd birthday'
print(message)

print(5+3)
print(10-2)
print(2*4)
print(16/2)

# hi to everybody
print ("Hi Everybody") # these is greeting

import this

bicycles=['treck','regular','hero','atlas']
print (bicycles)

bicycles=['treck','regular','hero','atlas']
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[2])
print(bicycles[1].upper())
print(bicycles[3].lower())
print (bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])


biy=['atlas','hero','herculas','ranger','ladies','thonder','gear']
print(biy[4].title())
print(biy)
message=('My first bicycle is '+ biy[0].upper()+'.'+'i ride along with my friend')
print(message)

alpha=['a', 'b', 'c', 'd', 'e', 'f','g','h']
print (alpha[2])
print(alpha[-2])
message=('my name start with letter '+alpha[0].upper()+' and my last name start with letter '+alpha[-2].upper())
print(message)
print(alpha[0]+alpha[2]+alpha[-1]+alpha[5]+' this is good practice for my study')
print(message,'.i love my self',' . During training in python i study various methods of oprations ')

alpha=['a', 'b', 'c', 'd', 'e', 'f','g','h']
print(alpha)
alpha[1]='x'
print(alpha)
alpha[-2]='z'
print(alpha)

alpha=['a', 'b', 'c', 'd', 'e', 'f','g','h']
alpha.append('k')
print(alpha)
alpha.append('s')
print(alpha)

gun=[]
print (gun)
gun.append('shotgun')
gun.append('automated')
gun.append('revolwer')
gun.append('german')
gun.append('desi katta')
gun.append('brahmose')
print(gun)
gun.insert(2,'rocket')
print(gun)
gun.insert(4,'agni1')
print(gun)

del gun[1]
print(gun)

gun=['shotgun', 'rocket', 'revolwer', 'agni1', 'german', 'desi katta', 'brahmose','tank']
print(gun)
popp_gun=gun.pop()
print(gun)
print(popp_gun)
gun=['shotgun', 'rocket', 'revolwer', 'agni1', 'german', 'desi katta', 'brahmose','tank']
last_woned=gun.pop()
print('The last weapon i hold was '+last_woned.upper()+'.')

third_woned=gun.pop(4)
print('The third weapon i hold was '+third_woned.upper()+'.')
gun=['shotgun', 'rocket', 'revolwer', 'agni1', 'german', 'desi katta', 'brahmose','tank']
print(gun)
removed_item=gun.remove('desi katta')
print(gun)
print(removed_item)