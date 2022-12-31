def i(first_name, last_name):
    full_name = first_name+" "+last_name
    return full_name.title()
while True:
    print("\n Tell me your name")
    print("\n if you want stop it write quite")
    f_name = input("first_name:")
    if f_name == "quite":
        break
    l_name = input("last_name:")
    if l_name == "quite":
        break
    full_name = i(f_name, l_name)
    print("hello "+full_name+"!")


def greet_user(names):
    for i in names:
        mess = "\n hello my friend "+i.title()+"\n how are you?"
        print(mess)


user = ['amol', 'atul', 'girish']
greet_user(user)
