from datetime import timedelta, datetime

def add_msg(date, msg):
    with open(f'output_files/{date}.txt', 'w+') as f:
        f.write(msg)


def get_event_duration(event_duration, event_duration_type):
    if event_duration_type == 'Hour':
        event_duration = round(event_duration * 60, 2)
    elif event_duration_type == 'Day':
        event_duration = round(event_duration * (24 * 60), 2)
    else:
        event_duration = event_duration
    return event_duration


def get_snooze_duration(snooze_duration, snooze_type):
    if snooze_type == 'Hour':
        snooze_duration = round(snooze_duration * 60, 2)
    elif snooze_type == 'Day':
        snooze_duration = round(snooze_duration * (24 * 60), 2)
    else:
        snooze_duration = snooze_duration
    return snooze_duration


def snooze_value(include_free_event, snooze_days, next_day, title, free_event_names, busy_event_names):
    if include_free_event:
        if len(snooze_days) > 0:
            if next_day.strftime('%A') in snooze_days:
                if title in free_event_names + busy_event_names:
                    return True
                else:
                    return False
        else:
            if title in free_event_names + busy_event_names:
                return True
            else:
                return False
    else:
        if len(snooze_days) > 0:
            if next_day.strftime('%A') in snooze_days:
                if title in busy_event_names:
                    return True
                else:
                    return False
        else:
            if title in busy_event_names:
                return True
            else:
                return False


def time_gaps(start_date, date_ranges, end_date):
    gaps = []
    eventStarts = [i[0] for i in date_ranges]
    eventEnds = [i[1] for i in date_ranges]
    
    if eventStarts[0] - start_date > timedelta(minutes=0):
        gaps.append((start_date, eventStarts[0]))
    
    for v in zip(eventStarts[1:], eventEnds[:-1]):
        if v[1] < v[0]:
            gaps.append((v[1], v[0]))
    
    if end_date - eventEnds[-1] > timedelta(minutes=0):
        gaps.append((eventEnds[-1], end_date))
    return gaps


def findCommon(list1, list2, minLength=timedelta(minutes=0)):
    newList = []
    for range1 in list1:
        for range2 in list2:
            overlapStart = max(range1[0], range2[0]) # the latest start time
            overlapEnd = min(range1[1], range2[1]) # the earliest end time
            if overlapEnd - overlapStart >= minLength:
                newList.append((overlapStart, overlapEnd))
    return newList


def reduce(listOfLists, minLength):
    if len(listOfLists) > 2:
        return reduce([findCommon(listOfLists[0], listOfLists[1], minLength)] + listOfLists[2:], minLength)
    elif len(listOfLists) == 2:
        return findCommon(listOfLists[0], listOfLists[1], minLength)
    if len(listOfLists) == 1:
        for _range in listOfLists:
            for i in _range:
                if i[1] - i[0] > minLength:
                    return [i]


def merge(ranges):
    ranges = list(sorted(ranges, key= lambda x: x[0]))
    saved = list(ranges[0])
    for range_set in ranges:
        if range_set[0] <= saved[1]:
            saved[1] = max(saved[1], range_set[1])
        else:
            yield tuple(saved)
            saved[0] = range_set[0]
            saved[1] = range_set[1]
    yield saved


def merge_range(ranges):
    range_output = list(merge(ranges))
    range_output[-1] = tuple(range_output[-1])
    return range_output
