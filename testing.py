from datetime import timedelta, datetime
from packages.utils import time_gaps, merge_range, reduce, get_lowtide
# c = CalendarEvent('lehrer', '/json_files/lehr.json', 'lehrercal3@gmail.com')
# ranges = [
#     [(datetime(2022, 6, 2, 9, 0), datetime(2022, 6, 2, 9, 30)), (datetime(2022, 6, 2, 11, 0), datetime(2022, 6, 2, 12, 10)),  (datetime(2022, 6, 2, 13, 0), datetime(2022, 6, 2, 14, 10))],
#     [
#         (datetime(2022, 6, 2, 5, 9), datetime(2022, 6, 2, 6, 56)), (datetime(2022, 6, 2, 15, 37), datetime(2022, 6, 2, 17, 24)), 
#         (datetime(2022, 6, 2, 9, 5), datetime(2022, 6, 2, 9, 40))
#     ],
#     [(datetime(2022, 6, 2, 9, 9), datetime(2022, 6, 2, 9, 30)), (datetime(2022, 6, 2, 4, 41, 3), datetime(2022, 6, 2, 6, 33, 3))],
#     [(datetime(2022, 6, 2, 9, 10), datetime(2022, 6, 2, 9, 20)), (datetime(2022, 6, 2, 20, 0), datetime(2022, 6, 2, 20, 23, 24))]
# ]
# duration = timedelta(minutes=30)

# print(reduce([ranges[0]], duration))

date = datetime(2022, 6, 9)

a = get_lowtide(date)

print(a)