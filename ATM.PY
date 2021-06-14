# print("welcome")
# print("please insert your code")
# print("please do not remove leave your card inserted during the entire transection ")
# print("please enter your pin number")
pin=int(input("enter the  pin number"))
total_balence=455897
if pin==8888:
    transection=input("enter the transection type\n1.case withdrowl\n2.balence inquary\n3.diposite\n4.quit")
    if transection=="1":
        print("case withdrowl")
        print("enter your amount")
        amount=int(input("enter the your amount"))
        if amount<=total_balence  and amount>0:
            print("take your case")
            left_amount=total_balence-amount
            print("your left balence",left_amount)
        else:
            print(" your money is not availble in account")
    elif transection=="2":
        print(total_balence)
    elif transection=="3":
        print("enter your diposit money")
        diposit_money=int(input("enter the your diposit money"))
        total_diposit=diposit_money+total_balence
        print(totle_diposit)
    elif transection=="4":
        print("exited")
    else:
        print("choose only vailed transection")
else:
    print("your pin is wrong")
