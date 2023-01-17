def formated_name(f_name,l_name):
    full_name = f_name+" "+l_name
    return full_name.title()

musician = formated_name('amol', 'gawade')
print(musician)


def form_name(f_name,l_name,m_name=""):
    if m_name:
        full_name = f_name+" "+m_name+' '+l_name
    else:
        full_name = f_name+" "+l_name
    return full_name.title()


musician = form_name('amol', 'gawade',  'shivaji')
print(musician)

mus = form_name('amol', 'gawade')
print(mus)


def build_person(f_name, l_name, age=''):
    person = {'first': f_name, 'last': l_name}
    if age:
        person['age'] = age
    return person


musician = build_person('amol', 'gawade', age=str(27))

print(musician)

