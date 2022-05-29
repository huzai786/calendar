from packages.temp import get_temperature
from datetime import timedelta
from packages.event_date import CalendarEvent
from packages.script_utils import time_gaps
import datetime
# c = CalendarEvent('lehrer', '/json_files/lehr.json', 'lehrercal3@gmail.com')

# d = datetime.datetime(2022, 6, 2)
# start_date = datetime.datetime(2022, 6, 2, 7)
# end_date = datetime.datetime(2022, 6, 2, 12, 10)
# x, y = c.get_event_detail(start_date, end_date, False, [], d, True, 'go walk')
# print(x)
# print(y)


ranges = [
    (datetime.datetime(2022, 6, 2, 7, 0), datetime.datetime(2022, 6, 2, 9, 0)), 
    (datetime.datetime(2022, 6, 2, 7, 30), datetime.datetime(2022, 6, 2, 8, 15)), 
    (datetime.datetime(2022, 6, 2, 9, 30), datetime.datetime(2022, 6, 2, 11, 0)), 
]
# print(ranges[1:])
# print(ranges[:-1])
# d_r = []
for i, v in enumerate(zip(ranges, ranges[1:])):
    x, y = v
    if x[1] > y[0]:
        ranges.append((x[0], y[1]))
        idx = ranges.index(x)
        idy = ranges.index(y)
        ranges.pop(idx)
        ranges.pop(idy)
    # print(x)
    # print(y)
print(ranges)
