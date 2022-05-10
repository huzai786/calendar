from datetime import datetime
from datetime import timedelta
from packages.event_date import CalendarEvent


# date = datetime.now().replace(second=0, minute=0, hour=0, microsecond=0)
# print(date)

name = 'lehrer'
path = '/json_files/lehr.json'
ide = 'lehrercal3@gmail.com'
c = CalendarEvent(name, path, ide)

start = datetime(2022, 5, 16, 6, 35)
end = start + timedelta(minutes=20)

i, x = c.calendar_event_func(start, end)

print(i, x)