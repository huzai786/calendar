from datetime import datetime, timedelta
from packages.temp import get_temperature
from packages.event_date import CalendarEvent
from packages.script_utils import reduce

from packages.filters import (
    temperature_filter,
    lowtide_filter,
    window_filter,
    sunrise_filter,
    sunset_filter
)


def main_func(title, days_to_look, calender_ids, days, filter_data, event_duration,
            snooze_duration, apply_snooze, snooze_days, include_free_event):
    event_in_all_cal_msg = ''
    for i in calender_ids:
        path = i.get('token_url')
        name = i.get('name')
        # Google calender from the id
        calendar = CalendarEvent(name, path, i.get('id'))
        calender_title = i.get('title')
        possible_date_message = f'Event: "{title}" \nCalender = {name}: {calender_title}\n'
        days_searched = 0
        date = datetime.now().strftime('%Y-%m-%d')
        initial_date = datetime.strptime(date, '%Y-%m-%d')
        while True:
            temp_check = None
            time_ranges = []
            if days_searched == days_to_look:
                break
            next_day = initial_date.replace(hour=0, minute=0)
            if next_day.strftime('%A') in days:
                days_searched += 1
                if any(['Temperature' in _dict.values() for _dict in filter_data]):
                    values = [(v.get('x1'), v.get('x2')) for v in filter_data if 'Temperature' in v.values()][0]
                    temperature = get_temperature(next_day)
                    get_temp = str((temperature * 9/5) + 32)
                    temp_check = temperature_filter(values, get_temp)
                    if temp_check is False:
                        initial_date += initial_date + timedelta(days=1)
                        continue


                if any(['Window' in _dict.values() for _dict in filter_data]):
                    values = [(v.get('x1'), v.get('x2')) for v in filter_data if 'Window' in v.values()][0]
                    time_range, snooze_check = window_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event)
                    if snooze_check is True:
                        initial_date += timedelta(days=snooze_duration)
                        continue
                    if time_range is not None: time_ranges.append(time_range)


                if any(['Low Tide' in _dict.values() for _dict in filter_data]):
                    values = [(v.get('x1'), v.get('x2')) for v in filter_data if 'Low Tide' in v.values()][0]
                    values = tuple(int(v) if v is not None else None for v in values)
                    time_range, snooze_check = lowtide_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event)
                    if snooze_check is True:
                        initial_date += timedelta(days=snooze_duration)
                        continue
                    if time_range is not None: time_ranges.append(time_range)


                if any(['Sunrise' in _dict.values() for _dict in filter_data]):
                    values = [(v.get('x1'), v.get('x2')) for v in filter_data if 'Sunrise' in v.values()][0]
                    values = tuple(int(v) if v is not None else None for v in values)
                    time_range, snooze_check = sunrise_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event)
                    if snooze_check is True:
                        initial_date += timedelta(days=snooze_duration)
                        continue
                    if time_range is not None:time_ranges.append(time_range)


                if any(['Sunset' in _dict.values() for _dict in filter_data]):
                    values = [(v.get('x1'), v.get('x2')) for v in filter_data if 'Sunset' in v.values()][0]
                    values = tuple(int(v) if v is not None else None for v in values)
                    time_range, snooze_check = sunset_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event)
                    if snooze_check is True:
                        initial_date += timedelta(days=snooze_duration)
                        continue
                    if time_range is not None:time_ranges.append(time_range)
                duration_of_event = timedelta(minutes=event_duration)
                print('time_ranges', time_ranges)
                slot = reduce(time_ranges, minLength=duration_of_event)
                print('slot', slot)
                if slot != []:
                    time = slot[0]
                    start_time = time[0]
                    start = start_time.strftime('%m-%d-%Y %I %p %M minutes')
                    end_time = time[1]
                    end = end_time.strftime('%m-%d-%Y %I %p %M minutes')
                    time_msg = f'from {start} to {end}'
                else:
                    next_day = next_day.strftime('%m-%d-%Y')
                    time_msg = f'no possible common time on {next_day}'
                    
                possible_date_message += time_msg + '\n--------------------------------------------------------\n'
            initial_date += timedelta(days=1)

        event_in_all_cal_msg += possible_date_message 
        
    return event_in_all_cal_msg


if __name__ == '__main__':
    main_func()
