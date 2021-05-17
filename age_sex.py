age=int(input("enter the number"))
sex=input("enter the number")
if age>=18 and age<=30:
    if sex=="male":
        print("700 wages")
elif age>=18 and age<=30:
    if sex=="female":
        print("750 wages")
elif age>=30 and age<=40:
    if sex=="male":
        print("800 wages")
elif age>=30 and age<=40:
    if sex=="female":
        print("850 wages")
else:
     print("nothing")
    
