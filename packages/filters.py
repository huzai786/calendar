

def temperature_filter(values, get_temp):
    if values[0] is not None and values[1] is None:
        
        if get_temp > values[0]:
            return True
        else:
            return False
            
    if values[0] is None and values[1] is not None:
        
        if get_temp < values[1]:
            return True
        else:
            return False
            
    if values[0] is not None and values[1] is not None:
        
        if (get_temp > tempx1) and (get_temp < tempx2):
            return True
        else:
            return False


def window_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event):
    schedule_date = None

    if values[0] is not None and values[1] is None:

        x = datetime.strptime(
            values[0], '%I:%M %p')

        start_date = datetime.combine(
            next_day.date(), x.time())
        end_date = start_date + \
            timedelta(minutes=event_duration)

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

                if title in events and (next_day.strftime('%A') in snooze_days):
                    return None, True

                else:
                    return None, False
        else:
            return None, False

    if values[0] is not None and values[1] is None:
        x = datetime.strptime(
            values[1], '%I:%M %p')

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

    if (values[0] is not None) and (values[1] is not None):

        x = datetime.strptime(
            values[0], '%I:%M %p')

        y = datetime.strptime(
            values[1], '%I:%M %p')

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


def sunrise_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event):
    sun_riset_info = ZipInfo(92009)

    """Function that return datetime of the sunrise of the input date"""

    get_sunrise_info = sun_riset_info.get_sunrise(next_day)
    schedule_date = None

    if values[0] != 0 and values[1] == 0:

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

    if values[1] != 0 and values[0] == 0:

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


def sunset_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event):
    """function that return datetime of the sunrise of the input date"""
    sun_riset_info = ZipInfo(92009)

    get_sunset_info = sun_riset_info.get_sunset(
        next_day)

    schedule_date = None
    print(get_sunset_info)
    if values[0] != 0 and values[1] == 0:

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

    if values[1] != 0 and values[0] == 0:

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


def lowtide_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event):
    """Function that return datetime of the low tide of the input date"""

    tide_info = get_lowtide(next_day)

    schedule_date = None

    if values[0] != 0 and values[1] == 0:
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

    if values[1] != 0 and values[0] == 0:
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


