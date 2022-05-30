from packages.temp import get_temperature
from datetime import timedelta, datetime
from packages.event_date import CalendarEvent
from packages.script_utils import time_gaps, merge_range
import datetime
# c = CalendarEvent('lehrer', '/json_files/lehr.json', 'lehrercal3@gmail.com')

# ranges = [
#     [(datetime(2022, 6, 2, 9, 0), datetime(2022, 6, 2, 9, 30)), (datetime(2022, 6, 2, 11, 0), datetime(2022, 6, 2, 12, 10))],
#     [(datetime(2022, 6, 2, 5, 9), datetime(2022, 6, 2, 6, 56)), (datetime(2022, 6, 2, 15, 37), datetime(2022, 6, 2, 17, 24))],
#     [(datetime(2022, 6, 2, 4, 41, 3), datetime(2022, 6, 2, 6, 33, 3))],
#     [(datetime(2022, 6, 2, 20, 0), datetime(2022, 6, 2, 20, 23, 24))]
# ]


def compare_lists(list1, list2, duration):
    
    gap_list = []
    for x in list1:
        for y in list2:
            if x[0] < y[0] and y[0] < x[1] < y[1]:
                gap_list.append((y[0], x[1]))

            if y[0] < x[0] < y[1] and y[0] < x[1] < y[1]:
                gap_list.append((y[0], y[1]))

            if y[0] < x[0] < y[1] and y[1] > x[1]:
                gap_list.append((x[0], x[1]))

            if x[0] < y[0] < x[1] and x[0] < y[1] < x[1]:
                gap_list.append((y[0], y[1]))
                
    common_time = [t for t in gap_list if (t[1] - t[0]) > duration]
    return common_time


duration = timedelta(minutes=20)
ranges = [
    [(datetime.datetime(2022, 6, 2, 9, 0), datetime.datetime(2022, 6, 2, 9, 30)),(datetime.datetime(2022, 6, 2, 11, 0), datetime.datetime(2022, 6, 2, 12, 10))],
    [(datetime.datetime(2022, 6, 2, 5, 9), datetime.datetime(2022, 6, 2, 6, 56)), (datetime.datetime(2022, 6, 2, 15, 37),datetime.datetime(2022, 6, 2, 17, 24)),  (datetime.datetime(2022, 6, 2, 15, 37), datetime.datetime(2022, 6, 2, 9, 25))],
]

ret = compare_lists(ranges[0], ranges[1], duration)
print(ret)
# product_lists = []
# for x, y in zip(ranges, ranges[1:]):
#     product = compare_lists(x, y)
#     product_lists.append(product)
# print(product_lists)

# def findCommon(list1, list2, minLength=timedelta(minutes=0)):
#     newList = []
#     for range1 in list1:
#         for range2 in list2:
#             try:
#                 print(range2)
#                 print(range1)
#                 overlapStart = max(range1[0], range2[0]) # the latest start time
#                 overlapEnd = min(range1[1], range2[1]) # the earliest end time
#                 if overlapEnd - overlapStart > minLength:
#                     newList.append((overlapStart, overlapEnd))
#                 return newList
#             except TypeError as e:
#                 break

# def reduce(listOfLists, minLength=timedelta(minutes=0)):
#     if len(listOfLists) > 2:
#         return reduce(findCommon(listOfLists[0], listOfLists[1], minLength) + listOfLists[2:], minLength)
#     else:
#         return findCommon(listOfLists[0], listOfLists[1], minLength)

# duration = timedelta(minutes=20)


# ranges = [
#     [(datetime(2022, 6, 2, 9, 0), datetime(2022, 6, 2, 9, 30)), (datetime(2022, 6, 2, 11, 0), datetime(2022, 6, 2, 12, 10))],
#     [(datetime(2022, 6, 2, 9, 0), datetime(2022, 6, 2, 9, 30)), (datetime(2022, 6, 2, 15, 37), datetime(2022, 6, 2, 17, 24))],
#     [(datetime(2022, 6, 2, 9, 0), datetime(2022, 6, 2, 9, 0))],
# ]

# print(reduce(ranges, duration))
