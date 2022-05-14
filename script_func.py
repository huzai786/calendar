from datetime import datetime, timedelta
from packages.temp import get_temperature
from packages.event_date import CalendarEvent
from packages.check_filter import set_filters



def main_func(title, days_to_look, calender_ids, days, filter_data, event_duration, 
                        snooze_duration, apply_snooze, snooze_days, include_free_event):

    event_in_all_cal_msg = ''
    for i in calender_ids:
        path = i.get('token_url')
        name = i.get('name')
        calendar = CalendarEvent(name, path, i.get('id'))  # Google calender from the id
        calender_title = i.get('title')
        possible_date_message = f'Event: "{title}" \nCalender = {name}: {calender_title}\n'
        for filteri in filter_data:
            filter_name = filteri.get('filter_name')
            filter_detail = filteri.get('filter_detail')
            x1 = filteri.get('x1')
            x2 = filteri.get('x2')
            temperature_included = filteri.get('temperature_included') 
            tempx1 = int(filteri.get('tempX1') or 0)
            tempx2 = int(filteri.get('tempX2') or 0)
            days_searched = 0
            date = datetime.now().strftime('%Y-%m-%d')
            initial_date = datetime.strptime(date, '%Y-%m-%d')
            dates_available = []
            while True:
                if days_searched == days_to_look:
                    break
                next_day = initial_date.replace(hour=0, minute=0)
                # List of days eg. ['Monday', 'Tuesday', etc]
                if next_day.strftime('%A') in days:
                    days_searched += 1
                    if temperature_included is True:
                        temperature = get_temperature(next_day)
                        get_temp = (temperature * 9/5) + 32
                        
                        if tempx1 != 0 and tempx2 == 0:
                            if get_temp > tempx1:
                                initial_date, possible_date = set_filters(
                                    title, calendar, filter_name, x1, x2, event_duration, 
                                        snooze_duration, apply_snooze, snooze_days, next_day, include_free_event)
                                initial_date = initial_date
                                
                                if possible_date is not None:
                                    dates_available.append(possible_date)

                            else:
                                initial_date += timedelta(days=1)
                                continue

                        if tempx2 != 0 and tempx1 == 0:
                            if get_temp < tempx2:
                                print('yes')
                                initial_date, possible_date = set_filters(
                                    title, calendar, filter_name, x1, x2, event_duration, 
                                        snooze_duration, apply_snooze, snooze_days, next_day, include_free_event)

                                initial_date = initial_date
                                
                                if possible_date is not None:
                                    dates_available.append(possible_date)

                            else:
                                initial_date += timedelta(days=1)
                                continue

                        if tempx1 != 0 and tempx2 != 0:
                            print('not not None')
                            print(tempx1, get_temp, tempx2)
                            if (get_temp > tempx1) and (get_temp < tempx2):
                                print('its not here')
                                initial_date, possible_date = set_filters(
                                    title, calendar, filter_name, x1, x2, event_duration, 
                                        snooze_duration, apply_snooze, snooze_days, next_day, include_free_event)

                                initial_date = initial_date
                                
                                if possible_date is not None:
                                    dates_available.append(possible_date)
                                        
                            else:
                                initial_date += timedelta(days=1)
                                continue

                    else:           # POSSIBLE DATE IS LIST
                        initial_date, possible_date = set_filters(
                            title, calendar, filter_name, x1, x2, event_duration, 
                                    snooze_duration, apply_snooze, snooze_days, next_day, include_free_event)
                        initial_date = initial_date
                        
                        if possible_date is not None:
                            dates_available.append(possible_date)
                        
                        
                initial_date += timedelta(days=1)
            d = dates_available or ['No possible date']
            s = '\n------------------------\n'.join(d)
            message = f'Filter: {filter_detail} \n' + '--------------------------\n' + s + \
                '\n--------------------------' + \
                '\n===============================================\n'
            possible_date_message += message
        event_in_all_cal_msg += possible_date_message    
        
    return event_in_all_cal_msg



if __name__ == '__main__':
    main_func()
