def formated_name(f_name,l_name):
    full_name = f_name+" "+l_name
    return full_name.title()

while True:
    print("\nTell me your name")
    print("type 'q' to quite")

    f_name = input("first name :-")
    if f_name == 'q':
        break
    l_name = input("last name :- ")
    if l_name == 'q':
        break
    name = formated_name(f_name,l_name)
    print("\nhello "+name + "!")



