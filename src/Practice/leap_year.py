'# to check given year is leap or not '''

year = int(input("Please enter the year:-"))
if (year % 100) == 0:
    if (year % 400) == 0:
        print(str(year)+" year is leap")
    else:
        print(str(year)+" year is not leap")
elif (year % 4) == 0:
    print(str(year)+" year is leap")
else:
    print(str(year)+" year is not leap")
