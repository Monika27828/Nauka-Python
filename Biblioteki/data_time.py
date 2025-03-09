import datetime
print(datetime.today())
now = datetime.datetime.now()
formated_date = now.strftime('%m-%Y-%d')
print(formated_date)