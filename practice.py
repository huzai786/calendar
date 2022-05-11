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

start = datetime(2022, 5, 16, 6, 35)
end = start + timedelta(minutes=20)

v = c.get_event_detail('ksml00onhbhe9bu4kmqil34scg@google.com')

# print(i, x)
print(v)

# for i in range(15):
#     a = get_temperature(date + timedelta(days=i))
#     print(a)

