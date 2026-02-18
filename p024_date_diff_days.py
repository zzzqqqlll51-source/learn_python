import datetime

def get_diff_days(pdate,days):
    pdate_obj = datetime.datetime.strptime(pdate,"%Y-%m-%d")
    timegap = datetime.timedelta(days=days)
    result_time = pdate_obj - timegap
    return result_time.strftime("%Y-%m-%d")

print(get_diff_days("2025-2-15",1))
print(get_diff_days("2025-2-15",10))
print(get_diff_days("2025-2-1",9))
print(get_diff_days("2025-2-15",4))