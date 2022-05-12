from datetime import datetime
from datetime import timedelta
from packages.event_date import CalendarEvent
from intervaltree import IntervalTree, Interval


name = 'lehrer'
path = '/json_files/lehr.json'
ide = 'lehrercal3@gmail.com'
c = CalendarEvent(name, path, ide)

start = datetime(2022, 5, 19, 7, 0)
end = start + timedelta(hours=3.5)
x = c.get_event_detail(start, end)

print(start, x, end)

# tree = IntervalTree.from_tuples(x)
# print(tree)
# x = tree.remove_overlap(start, end)

# print(tree)
