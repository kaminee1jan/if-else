return_day=int(input('enter the return_day'))
return_month=int(input('enter the return_month'))
return_year=int(input('enter the return_year'))
sumbit_day=int(input('enter the sumbit_day'))
sumbit_month=int(input('enter the sumbit_month'))
sumbit_year=int(input('enter the sumbit_year'))
if return_year>sumbit_year or return_month>sumbit_month and return_day>sumbit_day:
 print(0)
elif return_day<sumbit_day:
 if return_month==sumbit_month and return_year==sumbit_year:
  print(15*(sumbit_day-return_day))
elif return_month<sumbit_month:
 if return_year==sumbit_year:
  print(30*(sumbit_month-return_year)*500)
elif return_year<sumbit_year:
 print(10000)
else:
 print('nothing')