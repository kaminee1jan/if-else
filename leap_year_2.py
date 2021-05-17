year=int(input('enter the year'))
if year%4==0:
 if year%100==0:
  if year%400==0:
   print('this is leap year')
  else:
   print('century year ')
 else:
  print('leap year' or 'cen year')
else:
 print('not leap year')