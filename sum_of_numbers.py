maximum=int(input("enter the number"))
total=0
number=1
while number<=maximum:
    if number%2==0:
        total=total+number
    number=number+1
print("the sum of even numbers",total)