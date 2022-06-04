from datetime import datetime, timedelta
from packages.calendar_event_function import CalendarEvent

from packages.utils import (
    reduce,
    get_temperature,
    get_free_time_message
    )

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
        
        path, name, calender_title, cal_id = i.get('token_url'), i.get('name'), i.get('title'), i.get('id')
        calendar = CalendarEvent(name, path, cal_id)  # GET CALENDAR INSTANCE FROM ID
        
        possible_date_message = f'Event: "{title}" \nCalender = {name}: {calender_title}\n==============================================\n'
        
        days_searched = 0
        
        initial_date = datetime.strptime(datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
        
        snooze_is_applied = False

        while True:
            print('-----------------------------')
            temp_check = None

            time_ranges = []

            if days_searched == days_to_look:
                break

            next_day = initial_date.replace(hour=0, minute=0)

            if next_day.strftime('%A') in days:
                
                print(f'checking the day {next_day.strftime("%m-%d-%Y")}')
                
                days_searched += 1

                if any(['Temperature' in _dict.values() for _dict in filter_data]):
                    values = [(v.get('x1'), v.get('x2'))
                                for v in filter_data if 'Temperature' in v.values()][0]
                    temperature = get_temperature(next_day)
                    get_temp = str((temperature * 9/5) + 32)
                    temp_check = temperature_filter(values, get_temp)
                    if temp_check is False:
                        time_ranges.append('temp_invalid')

                if any(['Window' in _dict.values() for _dict in filter_data]):
                    values = [(v.get('x1'), v.get('x2'))
                                for v in filter_data if 'Window' in v.values()][0]
                    time_range, snooze_check = window_filter(
                        values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event)
                    if snooze_check and not snooze_is_applied:
                        days_searched -= 1
                        snooze_is_applied = True
                        initial_date += timedelta(days=snooze_duration)
                        continue
                    time_ranges.append(time_range)

                if any(['Low Tide' in _dict.values() for _dict in filter_data]):
                    values = [(v.get('x1'), v.get('x2'))
                                for v in filter_data if 'Low Tide' in v.values()][0]
                    values = tuple(
                        int(v) if v is not None else None for v in values)
                    time_range, snooze_check = lowtide_filter(
                        values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event)
                    if snooze_check and not snooze_is_applied:
                        days_searched -= 1
                        snooze_is_applied = True
                        initial_date += timedelta(days=snooze_duration)
                        continue
                    time_ranges.append(time_range)

                if any(['Sunrise' in _dict.values() for _dict in filter_data]):
                    values = [(v.get('x1'), v.get('x2'))
                                for v in filter_data if 'Sunrise' in v.values()][0]
                    values = tuple(
                        int(v) if v is not None else None for v in values)
                    time_range, snooze_check = sunrise_filter(
                        values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event)
                    if snooze_check and not snooze_is_applied:
                        print('yes sunrise is true')
                        days_searched -= 1
                        snooze_is_applied = True
                        initial_date += timedelta(minutes=snooze_duration)
                        print(days_searched)
                        continue
                    time_ranges.append(time_range)

                if any(['Sunset' in _dict.values() for _dict in filter_data]):
                    values = [(v.get('x1'), v.get('x2'))
                                for v in filter_data if 'Sunset' in v.values()][0]
                    values = tuple(
                        int(v) if v is not None else None for v in values)
                    time_range, snooze_check = sunset_filter(
                        values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event)
                    if snooze_check and not snooze_is_applied:
                        days_searched -= 1
                        snooze_is_applied = True
                        initial_date += timedelta(days=snooze_duration)
                        continue
                    time_ranges.append(time_range)
                    
                print('time_ranges', time_ranges)
                
                time_msg = get_free_time_message(time_ranges, next_day, event_duration)
                
                possible_date_message += time_msg + '\n--------------------------------------------------------\n'
                
            initial_date += timedelta(days=1)

        event_in_all_cal_msg += possible_date_message

    return event_in_all_cal_msg


if __name__ == '__main__':
    main_func()

