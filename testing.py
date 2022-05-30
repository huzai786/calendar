from packages.temp import get_temperature
from datetime import timedelta
from packages.event_date import CalendarEvent
from packages.script_utils import time_gaps, merge_range
import datetime
# c = CalendarEvent('lehrer', '/json_files/lehr.json', 'lehrercal3@gmail.com')

def compare_lists(list1, list2):
    gap_list = []
    for x in list1:
        for y in list2:
            if (y[0] < x[0] and y[1] < x[1]):
                if y[1] - y[0] > duration:
                    gap_list.append(y)
            if (x[0] < y[0] and x[1] < y[1]):
                if x[1] - x[0] > duration:
                    gap_list.append(x)
    return gap_list


duration = timedelta(minutes=20)
ranges = [
    [(datetime.datetime(2022, 6, 2, 9, 0), datetime.datetime(2022, 6, 2, 9, 30)), (datetime.datetime(2022, 6, 2, 11, 0), datetime.datetime(2022, 6, 2, 12, 10))], 
    [(datetime.datetime(2022, 6, 2, 5, 9), datetime.datetime(2022, 6, 2, 6, 56)), (datetime.datetime(2022, 6, 2, 15, 37), datetime.datetime(2022, 6, 2, 17, 24))], 
    [(datetime.datetime(2022, 6, 2, 4, 41, 3), datetime.datetime(2022, 6, 2, 6, 33, 3))], 
    [(datetime.datetime(2022, 6, 2, 20, 0), datetime.datetime(2022, 6, 2, 20, 23, 24))]
    ]


product_lists = []
for x, y in zip(ranges, ranges[1:]):
    product = compare_lists(x, y)
    product_lists.append(product)
    
print(product_lists)

[
    [
        (datetime.datetime(2022, 6, 2, 5, 9), datetime.datetime(2022, 6, 2, 6, 56)), (datetime.datetime(2022, 6, 2, 9, 0), datetime.datetime(2022, 6, 2, 9, 30)),
        (datetime.datetime(2022, 6, 2, 5, 9), datetime.datetime(2022, 6, 2, 6, 56)), (datetime.datetime(2022, 6, 2, 11, 0), datetime.datetime(2022, 6, 2, 12, 10))
    ], 
    [
    (datetime.datetime(2022, 6, 2, 4, 41, 3), datetime.datetime(2022, 6, 2, 6, 33, 3)), (datetime.datetime(2022, 6, 2, 4, 41, 3), datetime.datetime(2022, 6, 2, 6, 33, 3))
    ],
    [
    (datetime.datetime(2022, 6, 2, 4, 41, 3), datetime.datetime(2022, 6, 2, 6, 33, 3))
    ]
]
