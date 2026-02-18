import datetime

curr_time = datetime.datetime.now()
print(curr_time,type(curr_time))

str_time = curr_time.strftime("%Y年%m月%d日 %H:%M:%S")
print("str_time  ",str_time)