from datetime import datetime
from datetime import timedelta
from packages.temp import get_temperature
from packages.event_date import CalendarEvent


# date = datetime.now().replace(second=0, minute=0, hour=0, microsecond=0)
# print(date)

name = 'lehrer'
path = '/json_files/lehr.json'
ide = 'lehrercal3@gmail.com'
c = CalendarEvent(name, path, ide)

start = datetime(2022, 5, 19, 7, 0)
end = start + timedelta(hours=3.5)
x = c.get_event_detail(start, end)

print(x)


