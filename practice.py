# from datetime import datetime
# from datetime import timedelta
# from packages.event_date import CalendarEvent
# from packages.script_utils import findFirstOpenSlot


# name = 'lehrer'
# path = '/json_files/lehr.json'
# ide = 'lehrercal3@gmail.com'
# c = CalendarEvent(name, path, ide)

# start = datetime(2022, 5, 19, 7, 0)
# end = start + timedelta(hours=4)
# x, y = c.get_event_detail(start, end)
# print(y)
# events = sorted(x)
# print(events)
# # z = findFirstOpenSlot(events, start, end, timedelta(minutes=20), y)
# # print(z)

num = [(2, 5), (3, 4), (4, 7), (5, 6), (6, 11), (10, 11)]
# desnum = []
# for a, b in enumerate(num):
#     print(b)
#     if b[a][0] > b[a + 1][1]:
#         print('yes')
num = [(2, 5), (3, 4), (4, 7), (5, 6), (6, 11), (10, 11)]
for a in enumerate(zip(*(iter(num),)*2)):
    print(a)
    
num = [(2, 5), (3, 4), (4, 7), (5, 6), (6, 11), (10, 11)]
# step 1: combine (2, 5), (3, 4)
num = [(2, 5), (4, 7), (5, 6), (6, 11), (10, 11)]
# step 2: combine (2, 5), (4, 7)
num = [(2, 7), (5, 6), (6, 11), (10, 11)]
# step 3: combine (2, 7), (5, 6)
num = [(2, 7), (5, 6), (6, 11), (10, 11)]
# step 4: combine (2, 7), (5, 6)
num = [(2, 7), (6, 11), (10, 11)]
# step 5: combine (2, 7), (6, 11)
num = [(2, 11), (10, 11)]
# step 6: combine (2, 11), (10, 11)
num = [(2, 11)]