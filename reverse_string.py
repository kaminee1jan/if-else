str=input("enter the string")
length=len(str) 
str_rev=""
while length>0:
    str_rev=str_rev+str[length-1]
    length=length-1
print(str_rev)