from packages.script_utils import time_gaps, merge_range, reduce
from datetime import datetime, timedelta


ranges = [
    [
        (datetime(2022, 6, 2, 9, 0), datetime(2022, 6, 2, 9, 30)), (datetime(2022, 6, 2, 11, 10), datetime(2022, 6, 2, 12, 10)),
        (datetime(2022, 6, 2, 13, 0), datetime(2022, 6, 2, 14, 10)), (datetime(2022, 6, 2, 14, 20), datetime(2022, 6, 2, 15, 10))
        ],
    
    [(datetime(2022, 6, 2, 5, 9), datetime(2022, 6, 2, 6, 56)), (datetime(2022, 6, 2, 15, 37), datetime(2022, 6, 2, 17, 24))],
    [(datetime(2022, 6, 2, 4, 41, 3), datetime(2022, 6, 2, 6, 33, 3))],
    [(datetime(2022, 6, 2, 20, 0), datetime(2022, 6, 2, 20, 23, 24))]
]
start = datetime(2022, 6, 2, 7, 0)
end = datetime(2022, 6, 2, 17, 0)
a = time_gaps(start, ranges[0], end)

print(a)

x = [
    [
        (datetime.datetime(2022, 6, 3, 5, 48), datetime.datetime(2022, 6, 3, 6, 0)), 
        (datetime.datetime(2022, 6, 3, 16, 9), datetime.datetime(2022, 6, 3, 18, 9))
    ]
]

