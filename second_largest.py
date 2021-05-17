a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter a number"))
if a>b and a<c or a<b and a>c:
    print(a,"a second largest")
elif b>a and b<c or b<a and b>c:
    print(b," b second largest")
elif c>a and c<b or c<a and b>b:
    print(c,"c second largest")