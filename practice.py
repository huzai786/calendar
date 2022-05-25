from packages.temp import get_temperature
from datetime import datetime, timedelta
from packages.event_date import CalendarEvent

c = CalendarEvent('lehrer', '/json_files/lehr.json', 'lehrercal3@gmail.com')
# c = CalendarEvent('khabib', '/json_files/khabib.json', 'en.pk#holiday@group.v.calendar.google.com')

d = datetime(2022, 5, 23)

start_date = datetime(2022, 5, 23, 2)
end_date = datetime(2022, 5, 23, 9)
x, y = c.get_event_detail(start_date, end_date, False, [], d, True, 'go walk')
print(x)
print(y)

