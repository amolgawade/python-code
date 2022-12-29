age = 70
if age < 4:
    price = 0
elif age > 18:
    price = 10
elif age >= 60:
    price = 20
else:
    price = 30


print("your entry fee is "+ str(price)+" rupee .")

gun = ['shotgun', 'rocket', 'revolver', 'agni1', 'german', 'desi katta', 'brahmose', 'tank']

if 'shotgun' in gun:
    print("take the gun ")
if 'tank' in gun:
    print("take your weapon")
if "agni1" in gun:
    print("issro zindabad")
if 'rocket launcher' in gun:
    print("this choice of your is worst ")

print("\n lets make some alien for tonight dinner:-")

for requested_gun in gun:
    if requested_gun == 'german':
        print("your requested weapon"+ requested_gun.title()+" not available now * ")
    else:
        print("adding weapon "+ requested_gun.upper()+" to your accessories ")

print("\n you can use it now !")

requested_gun1 = []
if requested_gun1:
    for gun in requested_gun1 :
        print("requested gun "+gun)
    else:
        print("\n are you sure that you want thar gun")

gun = ['shotgun', 'rocket', 'revolver', 'agni1', 'german', 'desi katta', 'brahmose', 'tank']
req_gun =['shotgun','desi katta','tank','agni']
for x in req_gun:
    if x in gun:
        print("your request to adding "+x.title()+" accept")
    else:
        print("sorry don't have that weapon : " +x.title())

user_list = ['Amol_gawade','Shivaji_gawade','Rohoni_gawade','Kanchan_gawade']
current_list = ['Amol_gawade','Shivaji_gawade']
for x in user_list:
    if x in current_list:
        print("welcome to the organisation , we are happy to help "+x.upper()+" have a good day")
        print("would you like to see status report")


