import datetime

birthday = "20070808"
birthday_date = datetime.datetime.strptime(birthday,"%Y%m%d")
print(birthday_date,type(birthday_date))

curr_time = datetime.datetime.now()

minus_date = curr_time - birthday_date
print(minus_date,type(minus_date)) 

print(minus_date.days)