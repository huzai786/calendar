from datetime import datetime, timedelta
from packages.temp import get_temperature
from packages.event_date import CalendarEvent
from packages.check_filter import set_filters
from packages.return_time import ret_time_slot
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
                
                if any(['Temperature' in _dict for _dict in filter_data]):
                    values = [(value.get('x1'), value.get('x2'))
                            for value in dictionary if value.get('Temperature')][0]
                    temperature = get_temperature(next_day)
                    get_temp = (temperature * 9/5) + 32
                    temp_check = temperature_filter(values, get_temp)
                    if temp_check is False:
                        initial_date += initial_date + timedelta(days=1)
                        continue


                if any(['Window' in _dict for _dict in filter_data]):
                    values = [(value.get('x1'), value.get('x2'))
                            for value in dictionary if value.get('Window')][0]
                    time_range, snooze_check = window_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event)
                    
                    if snooze_check is True:
                        initial_date += timedelta(days=snooze_duration)
                        continue
                    if time_range is not None: time_ranges.append(time_range)


                if any(['Low Tide' in _dict for _dict in filter_data]):
                    values = [(value.get('x1'), value.get('x2'))
                            for value in dictionary if value.get('Low Tide')][0]
                    time_range, snooze_check = lowtide_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event)
                    if snooze_check is True:
                        initial_date += timedelta(days=snooze_duration)
                        continue
                    if time_range is not None: time_ranges.append(time_range)


                if any(['Sunrise' in _dict for _dict in filter_data]):
                    values = [(value.get('x1'), value.get('x2'))
                            for value in dictionary if value.get('Sunrise')][0]
                    time_range, snooze_check = sunrise_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event)
                    if snooze_check is True:
                        initial_date += timedelta(days=snooze_duration)
                        continue
                    if time_range is not None: time_ranges.append(time_range)


                if any(['Sunset' in _dict for _dict in filter_data]):
                    values = [(value.get('x1'), value.get('x2'))
                            for value in dictionary if value.get('Sunset')][0]
                    time_range, snooze_check = sunset_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event)
                    if snooze_check is True:
                        initial_date += timedelta(days=snooze_duration)
                        continue
                    if time_range is not None: time_ranges.append(time_range)
                    
                slot_msg = ret_time_slot(time_ranges, event_duration)
                initial_date += timedelta(days=1)
                
                possible_date_message += slot_msg
                
        event_in_all_cal_msg += possible_date_message
        
    return event_in_all_cal_msg


if __name__ == '__main__':
    main_func()
