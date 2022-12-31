def name_form(first_name, last_name):
    """return with full name."""
    full_name = first_name+" "+last_name
    return full_name.title()


musician = name_form('amol', 'gawade')
print(musician)


def name_form(first_name, last_name, middle_name=" "):
    if middle_name:
        full_name = first_name+" "+middle_name+" "+last_name
    else:
        full_name = first_name+" "+last_name
    return full_name.title()
musician = name_form('Amol', 'gawade','shivaji')
print(musician)

musician = name_form('amol', 'gawade')
print(musician)


def i(first_name,last_name):
    person = {'first': first_name, 'last': last_name}
    return person


musician = i('amol', 'gawade')
print(musician)


def i(first_name,last_name, age=' '):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = i('amol', 'gawade', age=27)
print(musician)


def i(first_name, last_name):
    full_name = first_name+" "+last_name
    return full_name.title


while True:
    print("\n tell me your name:")
    f_name = input('first_name:')
    l_name = input('last_name:')
    form_name = i(f_name, l_name)
    print("hello "+form_name+"!")


def get_formatted_name(first_name, last_name):
   full_name = first_name + ' ' + last_name
   return full_name.title()


while True:
     print("\nPlease tell me your name:")
     f_name = input("First name: ")
     l_name = input("Last name: ")
     formatted_name = get_formatted_name(f_name, l_name)
     print("\nHello, " + formatted_name + "!")