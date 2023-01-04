
print("please do the following process to convert the distance")
while True:

    print("select the one of the following option"
          "\n 1) KM TO M"
          "\n 2) M TO KM")
    option = int(input("enter option = "))
    distance = float(input("enter the distance = "))
    if option == 1:
        x = (distance * 1000)
        print("The distance "+str(distance)+"km = "+str(x)+"m")
    elif option == 2:
        x = (distance/1000)
        print("The distance "+str(distance)+"m = "+str(x)+"km")
    else:
        print("invalid option selection ")