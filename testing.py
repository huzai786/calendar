from packages.temp import get_temperature
from datetime import timedelta
from packages.event_date import CalendarEvent
from packages.script_utils import time_gaps, merge_range
import datetime
# c = CalendarEvent('lehrer', '/json_files/lehr.json', 'lehrercal3@gmail.com')



ranges = [
    [(datetime.datetime(2022, 6, 2, 9, 0), datetime.datetime(2022, 6, 2, 9, 30)), (datetime.datetime(2022, 6, 2, 11, 0), datetime.datetime(2022, 6, 2, 12, 10))], 
    [(datetime.datetime(2022, 6, 2, 5, 9), datetime.datetime(2022, 6, 2, 6, 56)), (datetime.datetime(2022, 6, 2, 15, 37), datetime.datetime(2022, 6, 2, 17, 24))], 
    [(datetime.datetime(2022, 6, 2, 4, 41, 3), datetime.datetime(2022, 6, 2, 6, 33, 3))], 
    [(datetime.datetime(2022, 6, 2, 20, 0), datetime.datetime(2022, 6, 2, 20, 23, 24))]
]
"""
I am struggling to implement this sort of algorithm that finds a common time slot from the given list of sub lists, that list can have more than 1 sub list, up to 4, and also I have a event duration of for say, 20 minutes, i want to find a common time slot of 20 minutes, that satisfy all the sub list present.
the sample data is below:
```
ranges = [
    [(datetime.datetime(2022, 6, 2, 9, 0), datetime.datetime(2022, 6, 2, 9, 30)), (datetime.datetime(2022, 6, 2, 11, 0), datetime.datetime(2022, 6, 2, 12, 10))], 
    [(datetime.datetime(2022, 6, 2, 5, 9), datetime.datetime(2022, 6, 2, 6, 56)), (datetime.datetime(2022, 6, 2, 15, 37), datetime.datetime(2022, 6, 2, 17, 24))], 
    [(datetime.datetime(2022, 6, 2, 4, 41, 3), datetime.datetime(2022, 6, 2, 6, 33, 3))], 
    [(datetime.datetime(2022, 6, 2, 20, 0), datetime.datetime(2022, 6, 2, 20, 23, 24))]
]
```
the ranges are sorted, no overlapse

"""