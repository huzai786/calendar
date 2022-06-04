import requests
from datetime import timedelta, datetime
from meteostat import Point, Hourly
from astral import LocationInfo, sun



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
    
    if len(listOfLists) == 1:
        available_times = [i for i in listOfLists[0] if (i[1] - i[0]) > minLength]
        return available_times
    
    if len(listOfLists) == 2:
        return findCommon(listOfLists[0], listOfLists[1], minLength)
    
    if len(listOfLists) > 2:
        return reduce([findCommon(listOfLists[0], listOfLists[1], minLength)] + listOfLists[2:], minLength)


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


def get_temp(date):
    start = date + timedelta(days=1, hours=12)
    end = start + timedelta(hours=12)
    Carlsbad = Point(33.0954, -117.2619, 143.5)
    temp = Hourly(Carlsbad, start, end)
    data = temp.fetch().to_dict()
    y = data.get('temp')
    lis = [v for k, v in y.items() if v is not int()]
    try:
        return max(lis)
    except Exception as e:
        return None


def get_temperature(date):
    day = date
    while True:
        a = get_temp(day)
        if a != None:
            return a
            break
        if a == None:
            day = day - timedelta(days = 1)
            continue


def get_lowtide(date):
    begin_date = date.strftime('%Y%m%d')
    stop_date = (date + timedelta(days=0)).strftime('%Y%m%d') 
    url = f"https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date={begin_date}&end_date={stop_date}&station=9410230&product=predictions&datum=MLLW&time_zone=lst_ldt&interval=hilo&units=english&format=json"
    res = requests.get(url=url).json()
    tide_data = res.get('predictions')
    try:
        low_tide_value = [data.get('t') for data in tide_data if data.get('type') == 'L']
        return [datetime.strptime(i, '%Y-%m-%d %H:%M') for i in low_tide_value]


    except Exception as e:
        print('tide error', e)
        return 0


def get_sunrise(zipcode, for_date):
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid=7015d42a7df0d257dad429a045772ef2"
    res = requests.get(url=url).json()
    longitude = res.get('coord').get('lon')
    latitude = res.get('coord').get('lat')

    city = LocationInfo('Carlsbad', 'california', "US/Pacific", latitude, longitude)
    s = sun.sun(city.observer, date=for_date, tzinfo=city.timezone)
    return (s['sunrise']).replace(tzinfo=None, microsecond=0)


def get_sunset(zipcode, for_date):
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},us&appid=7015d42a7df0d257dad429a045772ef2"
    res = requests.get(url=url).json()
    longitude = res.get('coord').get('lon')
    latitude = res.get('coord').get('lat')

    city = LocationInfo('Carlsbad', 'california', "US/Pacific", latitude, longitude)
    s = sun.sun(city.observer, date=for_date, tzinfo=city.timezone)
    return (s['sunset']).replace(tzinfo=None, microsecond=0)


def get_free_time_message(time_ranges, next_day, event_duration):
    
    next_day = next_day.strftime('%m-%d-%Y')
    
    if not 'temp_invalid' in time_ranges and None in time_ranges:

        time_msg = f"extended event found for day {next_day}"
        
        return time_msg

    if 'temp_invalid' in time_ranges and not None in time_ranges:

        time_msg = f"Temperature filter not satisfied for day {next_day}"

        return time_msg
    
    if 'temp_invalid' and None in time_ranges:

        time_msg = f'temperature invalid and extended event found for day {next_day}'

        return time_msg
    
    if not 'temp_invalid' in time_ranges and not None in time_ranges:

        slot = reduce(time_ranges, minLength=timedelta(minutes=event_duration))

        if slot != []:

            start = slot[0][0].strftime('%m-%d-%Y %I %p %M minutes')

            end = slot[0][1].strftime('%m-%d-%Y %I %p %M minutes')

            time_msg = f'from {start} to {end}'
            
            return time_msg

        if slot is []:

            time_msg = f'no possible common time on {next_day}'

            return time_msg

