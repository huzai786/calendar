from datetime import datetime
from datetime import timedelta
from packages.event_date import CalendarEvent
from packages.script_utils import findFirstOpenSlot


name = 'lehrer'
path = '/json_files/lehr.json'
ide = 'lehrercal3@gmail.com'
c = CalendarEvent(name, path, ide)

start = datetime(2022, 5, 22, 0, 0)
end = start + timedelta(hours=23)
x, y = c.get_event_detail(start, end, True)
events = sorted(x)
# print(y)
print(events)

# num = [(2, 5), (3, 4), (4, 7), (5, 6), (6, 11), (10, 11)]


# x = datetime(2022, 5, 19, 9) - datetime(2022, 5, 19, 7)
# i = 1
# last_index = len(num) 
# while True:
#     if i == last_index:
#         i -= 1
#     a, b = num[0], num[i]
#     if a[1] > b[0]:
#         print(a[1])
#         print(b[0])
#         print('----')
#         num.remove(b)
#         print(num)
#     i += 1


startRange = [x[0] for x in events]
endRange = [x[1] for x in events]
print('start', startRange)
print('end', endRange)
lastEvent = endRange[-1]
duration = timedelta(minutes=30)
can_be = []                 # start of next, end of before
not_be = []
yess = []
for i, v in enumerate(zip(startRange[1:], endRange[:-1])):
    if v[0] > v[1]:
        gap = v[0] - v[1]
        if duration < gap:
            can_be.append(v[1])
    else:
        not_be.append(v[1])
        

for i, v in enumerate(can_be):
    if any(v > x for x in not_be):
        yess.append(v)
        

if duration < (end - lastEvent):
    print(lastEvent, False)
print(can_be)
print(not_be)
print(yess)