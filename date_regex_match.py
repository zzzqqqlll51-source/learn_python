import re

def date_is_right(date):
    return re.match("\d{4}-\d{2}-\d{2}",date) is not None

date1 = "2026-02-18"
date2 = "2025-3-12"
print(date_is_right(date1))
print(date_is_right(date2))