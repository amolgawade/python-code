def greet_user():
    """Display simple greeting."""
    print("hello")
greet_user()

def i(username):
    """Display simple greeting."""
    print("hello  :"+username.title())
i('amol')

def des_pet(ani_type, name):
    print("\ni have a "+ani_type)
    print("\n The name of my "+ani_type+" is :"+name.title())


des_pet('cat','tom')
des_pet('Dog', 'tukya')
des_pet(ani_type='cow', name='rani')
des_pet(name='raja', ani_type='bull')


def  des_pet(ani_type,  name='ninavi'):
    print("\ni have a "+ani_type)
    print("\n The name of my "+ani_type+" is :"+name.title())
des_pet(ani_type='dog')
