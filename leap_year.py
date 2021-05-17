year=int(input("enter the number"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("that is leap year")
        else:
            print("that is not leap year")
    else:
        print("that is leap year")
else:
    print("that is not leap year")
    