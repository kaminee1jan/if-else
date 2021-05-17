basic_salry=int(input("enter the salry"))
if basic_salry<=10000:
 g_s=basic_salry+basic_salry*0.2+basic_salry* 0.8
 print(g_s)
elif basic_salry<=20000:
 g_s=basic_salry+basic_salry*0.25*basic_salry*0.9
 print(g_s)
elif basic_salry>20000:
 g_s=basic_salry+basic_salry*0.3+basic_salry*0.95
 print(g_s)
else:
 print("nothing")