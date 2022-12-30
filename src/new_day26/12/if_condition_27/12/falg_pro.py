i = "\n tell me some thing i wiil repeat back to you: "
i += "\nEnter the 'quit' to end the program "
active = True
while active:
    message = input(i)
    if message == 'quit':
        active = False
    else:
        print(message)

i = "\n enter the city you visited :"
i += "\n Enter the 'quit to end the program"
while True:
    city = input(i)
    if city == 'quit':
        break
    else:
        print('i would live to go '+city.title()+":")
