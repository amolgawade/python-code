from cal_class import Calculator

while True:
    print("You can do add / sub / mul / div operation using this."
          " please enter 2 values to do these operation.")
    a = int(input("Enter the a number:-"))
    b = int(input("Enter the b number:- "))
    calc = Calculator(a, b)

    operation = int(input("Please enter the operation do you want:-"
                          "\n1:add\n2:sub\n3:mul\n4:div\n"))
    if operation == 1:
        print("the addition is "+str(calc.add()))
    elif operation == 2:
        print("the subtraction is "+str(calc.sub()))
    elif operation == 3:
        print("The multification is "+str(calc.mul()))
    elif operation == 4:
        print("The divison is "+str(calc.div()))
    else:
        print("invalid input")
