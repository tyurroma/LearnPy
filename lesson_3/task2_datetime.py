import datetime 

today = datetime.datetime.now()
print(today.strftime('%d.%m.%Y'))

delta = datetime.timedelta(days=1)
yesterday = today - delta
print(yesterday.strftime('%d.%m.%Y'))

delta = datetime.timedelta(days=31)
month_before = today - delta
print(month_before.strftime('%d.%m.%Y'))

date_string = '01/01/17 12:10:03.234567'
datetime_obj = datetime.datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(datetime_obj)