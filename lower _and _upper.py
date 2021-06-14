str=input("enter the string")
upper=0
lower=0
index=0
while index<len(str):
    if str[index]>="a" and str[index]<="z":
        lower=lower+1
    elif str[index]>="A" and str[index]<="Z":
        upper=upper+1
    index=index+1
print("lower case letters=",lower)
print("upper case letters=",upper)
