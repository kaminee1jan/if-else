amount = int(input('enter the amount'))
if amount<= 2000:
    discount = (amount * 0.5)
    print ("Paid Amount", amount-discount)
elif amount >=5000 and amount <=6000:
    discount = (amount * 0.25)
    print ("Paid Amount", amount-discount)
if amount >= 10000:
    discount = (amount * 0.35)
    print ("Paid Amount", amount-discount)
else:
    discount = (amount *0.50)
    print ("Paid Amount", amount-discount)