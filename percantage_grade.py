phy=int(input("enter the marks--"))
che=int(input("enter the marks--"))
bio=int(input("enter the marks--"))
math=int(input("enter the marks--"))
com=int(input("enter the marks--"))
total=phy+che+bio+math+com
per=total*100/500
if per>=90:
 print(per , "Grade A")
elif per>=80:
 print(per , "Grade B")
elif per>=70:
 print(per, "grade C")
elif per>=60:
 print(per, "grade D")
elif per>=40:
 print(per, "grade E")
elif per<=40:
 print(per, "grade F")
else:
 print("nothing")