current_no = 10
while current_no <= 20:
    print(current_no)
    current_no += 1


i = "\n tell me something i will repeat back after you : "
i += "\n enter 'quite' to end the program "
message = " "
while message != "quite":
    message = input(i)
    print(message)
