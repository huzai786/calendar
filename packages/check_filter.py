from datetime import datetime, timedelta
from packages.sunriset import ZipInfo
from packages.lowtide import get_lowtide
from packages.script_utils import findFirstOpenSlot



def set_window_filter(title, windowx1, windowx2, event_duration, calendar, next_day, snooze_days, 
                        apply_snooze, include_free_event):
    
    schedule_date = None

    if windowx1 is not None and windowx2 is None:

        x = datetime.strptime(
            windowx1, '%I:%M %p')

        start_date = datetime.combine(
            next_day.date(), x.time())
        print(start_date)
        end_date = start_date + \
            timedelta(minutes=event_duration)

        event_value, events = calendar.calendar_event_func(
            start_date, end_date, include_free_event)
        print('event_value, events', event_value, events)
        if event_value is None:

            schedule_date = start_date.strftime(
                '%A, %d, %B, %Y       %I:%M %p')

            return schedule_date, False

        if apply_snooze == True:

            if snooze_days == []:

                if title in events:

                    return None, True

                else:
                    return None, False

            if snooze_days != []:

                if title in events and (next_day.strftime('%A') in snooze_days):
                    return None, True

                else:
                    return None, False
        else:
            return None, False

    if windowx2 is not None and windowx1 is None:
        x = datetime.strptime(
            windowx2, '%I:%M %p')

        start_date = datetime.combine(
            next_day.date(), x.time())

        end_date = start_date - \
            timedelta(minutes=event_duration)

        event_value, events = calendar.calendar_event_func(
            end_date, start_date, include_free_event)

        if event_value is None:

            schedule_date = end_date.strftime(
                '%A, %d, %B, %Y       %I:%M %p')

            return schedule_date, False

        if apply_snooze == True:
            if snooze_days == []:

                if title in events:

                    return None, True

                else:
                    return None, False

            if snooze_days != []:

                if title in events and (next_day.strftime('%A') in snooze_days):
                    return None, True

                else:
                    return None, False
                
        else:
            return None, False

    if (windowx1 is not None) and (windowx2 is not None):

        x = datetime.strptime(
            windowx1, '%I:%M %p')

        y = datetime.strptime(
            windowx2, '%I:%M %p')

        start_date = datetime.combine(
            next_day.date(), x.time())
        
        end_date = datetime.combine(
            next_day.date(), y.time())
        
        date_ranges, event_names = calendar.get_event_detail(start_date, end_date, include_free_event)
        
        date, snooze = findFirstOpenSlot(date_ranges, start_date, end_date, timedelta(minutes=event_duration),
                                        event_names, title, apply_snooze, snooze_days, next_day)
        
        if date is not None:
            schedule_date = date.strftime(
                '%A, %d, %B, %Y       %I:%M %p')

            return schedule_date, False
        
        if snooze is True:
            return None, True
        
        return None, False

def set_sunrise_filter(title, sunrise1, sunrise2, event_duration, calendar, next_day, snooze_days
                        ,apply_snooze, include_free_event):

    sun_riset_info = ZipInfo(92009)

    """Function that return datetime of the sunrise of the input date"""

    get_sunrise_info = sun_riset_info.get_sunrise(next_day)
    schedule_date = None

    if sunrise1 != 0 and sunrise2 == 0:

        start_date = get_sunrise_info - \
            timedelta(minutes=sunrise1) - \
            timedelta(
                minutes=event_duration)

        end_date = get_sunrise_info - \
            timedelta(minutes=sunrise1)

        event_value, events = calendar.calendar_event_func(
            start_date, end_date, include_free_event)

        if event_value is None:

            schedule_date = start_date.strftime(
                '%A, %d, %B, %Y       %I:%M %p')

            return schedule_date, False

        if apply_snooze == True:

            if snooze_days == []:

                if title in events:

                    return None, True

                else:
                    return None, False

            if snooze_days != []:

                if title in events and (start_date.strftime('%A') in snooze_days):
                    return None, True

                else:
                    return None, False
        else:
            return None, False

    if sunrise2 != 0 and sunrise1 == 0:

        start_date = get_sunrise_info + \
            timedelta(minutes=sunrise2) + \
            timedelta(
                minutes=event_duration)

        end_date = get_sunrise_info + \
            timedelta(minutes=sunrise2)

        event_value, events = calendar.calendar_event_func(
            end_date, start_date, include_free_event)

        if event_value is None:

            schedule_date = end_date.strftime(
                '%A, %d, %B, %Y       %I:%M %p')

            return schedule_date, False

        if apply_snooze == True:

            if snooze_days == []:

                if title in events:

                    return None, True

                else:
                    return None, False

            if snooze_days != []:

                if title in events and (start_date.strftime('%A') in snooze_days):
                    return None, True

                else:
                    return None, False
        else:
            return None, False

def set_sunset_filter(title, sunset1, sunset2, event_duration, calendar, next_day, snooze_days
                        ,apply_snooze, include_free_event):
    """function that return datetime of the sunrise of the input date"""
    sun_riset_info = ZipInfo(92009)

    get_sunset_info = sun_riset_info.get_sunset(
        next_day)

    schedule_date = None
    print(get_sunset_info)
    if sunset1 != 0 and sunset2 == 0:

        start_date = get_sunset_info - \
            timedelta(
                minutes=sunset1) - timedelta(minutes=event_duration)

        end_date = get_sunset_info - \
            timedelta(minutes=sunset1)

        event_value, events = calendar.calendar_event_func(
            start_date, end_date, include_free_event)

        if event_value is None:

            schedule_date = start_date.strftime(
                '%A, %d, %B, %Y       %I:%M %p')

            return schedule_date, False

        if apply_snooze == True:

            if snooze_days == []:

                if title in events:

                    return None, True

                else:
                    return None, False

            if snooze_days != []:

                if title in events and (start_date.strftime('%A') in snooze_days):
                    return None, True

                else:
                    return None, False
        else:
            return None, False

    if sunset2 != 0 and sunset1 == 0:

        start_date = get_sunset_info + \
            timedelta(
                minutes=sunset2)

        end_date = get_sunset_info + \
            timedelta(minutes=sunset2) + timedelta(minutes=event_duration)
        event_value, events = calendar.calendar_event_func(
            start_date, end_date, include_free_event)
        if event_value is None:
            schedule_date = start_date.strftime(
                '%A, %d, %B, %Y       %I:%M %p')
            print('schedule_date', schedule_date)
            return schedule_date, False

        if apply_snooze == True:

            if snooze_days == []:

                if title in events:

                    return None, True

                else:
                    return None, False

            if snooze_days != []:

                if title in events and (start_date.strftime('%A') in snooze_days):
                    return None, True

                else:
                    return None, False
                
        else:
            return None, False

def set_lowtide_filter(title, lowtide1, lowtide2, event_duration, calendar, next_day, snooze_days,
                        apply_snooze, include_free_event):
    """Function that return datetime of the low tide of the input date"""

    tide_info = get_lowtide(next_day)

    schedule_date = None

    if lowtide1 != 0 and lowtide2 == 0:
        start_date = tide_info - timedelta(minutes=lowtide1) - \
            timedelta(
                minutes=event_duration)

        end_date = tide_info - \
            timedelta(minutes=lowtide1)

        event_value, events = calendar.calendar_event_func(
            start_date, end_date, include_free_event)

        if event_value is None:

            schedule_date = start_date.strftime('%A, %d, %B, %Y       %I:%M %p')

            return schedule_date, False

        if apply_snooze == True:

            if snooze_days == []:

                if title in events:

                    return None, True

                else:
                    return None, False

            if snooze_days != []:

                if title in events and (start_date.strftime('%M') in snooze_days):
                    return None, True

                else:
                    return None, False
                
        else:
            return None, False

    if lowtide2 != 0 and lowtide1 == 0:
        print('tide_info', tide_info)
        start_date = tide_info + \
            timedelta(minutes=lowtide2)
        print('start_date', start_date)
        end_date = tide_info + \
            timedelta(minutes=lowtide2) + \
            timedelta(
                minutes=event_duration)
        print('end_date', end_date)
        
        event_value, events = calendar.calendar_event_func(
            start_date, end_date, include_free_event)
        print('event_value, events: ', event_value, events)
        print('--------------------------------------')
        if event_value is None:

            schedule_date = start_date.strftime(
                    '%A, %d, %B, %Y       %I:%M %p')
            print('yes', schedule_date)
            return schedule_date, False

        if apply_snooze == True:

            if snooze_days == []:

                if title in events:

                    return None, True

                else:
                    return None, False

            if snooze_days != []:

                if title in events and (start_date.strftime('%A') in snooze_days):
                    return None, True

                else:
                    return None, False

        else:
            return None, False



def set_filters(title, calendar, filter_name, x1, x2, event_duration, snooze_duration, 
                    apply_snooze, snooze_days, next_day, include_free_event):

    if filter_name == 'Window':
        date_msg = None

        windowx1 = x1  # Get window x1 value from filter_data

        windowx2 = x2  # Get window x2 value from filter_data
        
        time_window_available, snooze_check = set_window_filter(  # Output datetime/None,  True/False
            title, windowx1, windowx2, event_duration, calendar, next_day, snooze_days, apply_snooze, include_free_event)
        
        if time_window_available is not None:
            date_msg = f'day: {time_window_available[:26]} \ntime: {time_window_available[-8:]}'
            
        if (date_msg is not None) and (snooze_check is True):

            initial_date = next_day + timedelta(minutes=snooze_duration) - timedelta(days=1)
            return (initial_date, date_msg)

        if (date_msg is not None) and (snooze_check is False):
            print('its here')
            return (next_day,  date_msg)

        else:
            return (next_day, None)

    if filter_name == 'Sunrise':
        date_msg = None

        sunrise1 = int(x1 or 0)  # Get sunrise x2 value from filter_data

        sunrise2 = int(x2 or 0)  # Get sunrise x2 value from filter_data

        sunrise_time_available, snooze_check = set_sunrise_filter(  # Output datetime/None,  True/False
            title, sunrise1, sunrise2, event_duration, calendar, next_day, snooze_days, apply_snooze, include_free_event)

        if sunrise_time_available is not None:
            date_msg = f'day: {sunrise_time_available[:26]} \ntime: {sunrise_time_available[-8:]}'

        if (date_msg is not None) and (snooze_check is True):

            initial_date = next_day + timedelta(minutes=snooze_duration) - timedelta(days=1)

            return (initial_date, date_msg)

        if (date_msg is not None) and (snooze_check is False):
            return (next_day,  date_msg)

        else:
            return (next_day, None)

    if filter_name == 'Sunset':
        date_msg = None

        sunset1 = int(x1 or 0)  # Get Sunset x1 value from filter_data

        sunset2 = int(x2 or 0)  # Get Sunset x2 value from filter_data

        sunset_time_available, snooze_check = set_sunset_filter(  # Output datetime/None,  True/False
            title, sunset1, sunset2, event_duration, calendar, next_day, snooze_days, apply_snooze, include_free_event)
        
        if sunset_time_available is not None:
            date_msg = f'day: {sunset_time_available[:26]} \ntime: {sunset_time_available[-8:]}'
            
        if (date_msg is not None) and (snooze_check is True):

            initial_date = next_day + timedelta(minutes=snooze_duration) - timedelta(days=1)
            return (initial_date, date_msg)

        if (date_msg is not None) and (snooze_check is False):
            return (next_day,  date_msg)

        else:
            return (next_day, None)

    if filter_name == 'Low Tide':

        date_msg = None

        lowtide1 = int(x1 or 0)  # Get lowtide x1 value from filter_data

        lowtide2 = int(x2 or 0)  # Get lowtide x2 value from filter_data

        lowtide_time_available, snooze_check = set_lowtide_filter(  # Output datetime/None,  True/False
            title, lowtide1, lowtide2, event_duration, calendar, next_day, snooze_days, apply_snooze, include_free_event)

        if lowtide_time_available is not None:

            date_msg = f'day: {lowtide_time_available[:26]} \ntime: {lowtide_time_available[-8:]}'

        if (date_msg is not None) and (snooze_check is True):

            initial_date = next_day + timedelta(minutes=snooze_duration) - timedelta(days=1)

            return (initial_date, date_msg)

        elif (date_msg is not None) and (snooze_check is False):
            return (next_day,  date_msg)

        else:
            return (next_day, None)

