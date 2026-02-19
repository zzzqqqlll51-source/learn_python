import datetime

def get_date_range(begin,end):
    date_list = []
    while begin <= end:
        date_list.append(begin)
        begin_obj = datetime.datetime.strptime(begin,"%Y-%m-%d")
        timegap_days1 = datetime.timedelta(days=1)
        begin = (timegap_days1 + begin_obj).strftime("%Y-%m-%d")
    return date_list

begin = "2026-01-22"
end = "2026-02-15"
date_list = get_date_range(begin,end)
print(date_list)
