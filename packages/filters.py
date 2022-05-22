from datetime import datetime, timedelta
from packages.sunriset import ZipInfo
from packages.lowtide import get_lowtide
from packages.script_utils import findFirstOpenSlot



def temperature_filter(values, get_temp):
    
    if values[0] is not None and values[1] is None:
        
        if get_temp >= values[0]:
            return True
        else:
            return False
            
    if values[0] is None and values[1] is not None:
        
        if get_temp <= values[1]:
            return True
        else:
            return False
            
    if values[0] is not None and values[1] is not None:
        
        if (get_temp >= tempx1) and (get_temp <= tempx2):
            return True
        else:
            return False


def window_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event):

    if values[0] is not None and values[1] is None:

        x = datetime.strptime(values[0], '%I:%M %p')
        start_date = datetime.combine(next_day.date(), x.time())
        end_date = start_date + timedelta(minutes=event_duration)
        time_range, snooze_check = calendar.get_event_detail(start_date, end_date, apply_snooze, snooze_days, next_day, include_free_event, title)
        
        return (time_range, snooze_check)

    if values[1] is not None and values[1] is None:
        x = datetime.strptime(values[1], '%I:%M %p')
        start_date = datetime.combine(next_day.date(), x.time())
        end_date = start_date - timedelta(minutes=event_duration)
        time_range, snooze_check = calendar.get_event_detail(start_date, end_date, apply_snooze, snooze_days, next_day, include_free_event, title)
        
        return (time_range, snooze_check)
        
    if (values[0] is not None) and (values[1] is not None):

        x = datetime.strptime(values[0], '%I:%M %p')
        y = datetime.strptime(values[1], '%I:%M %p')

        start_date = datetime.combine(next_day.date(), x.time())
        end_date = datetime.combine(next_day.date(), y.time())
        time_range, snooze_check = calendar.get_event_detail(start_date, end_date, apply_snooze, snooze_days, next_day, include_free_event, title)
        
        return (time_range, snooze_check)


def sunrise_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event):
    """Function that return datetime of the sunrise of the input date"""
    sun_riset_info = ZipInfo(92009)
    get_sunrise_info = sun_riset_info.get_sunrise(next_day)
    
    if values[0] is not None and values[1] is None:

        start_date = get_sunrise_info - timedelta(minutes=values[0]) - timedelta(minutes=event_duration)
        end_date = get_sunrise_info - timedelta(minutes=values[0])
        time_range, snooze_check = calendar.get_event_detail(start_date, end_date, apply_snooze, snooze_days, next_day, include_free_event, title)
        
        return (time_range, snooze_check)

    if values[1] is not None and values[0] is None:
        start_date = get_sunrise_info + timedelta(minutes=values[1]) 
        end_date = get_sunrise_info + timedelta(minutes=values[1]) + timedelta(minutes=event_duration)
        time_range, snooze_check = calendar.get_event_detail(start_date, end_date, apply_snooze, snooze_days, next_day, include_free_event, title)
        
        return (time_range, snooze_check)

    if values[0] is not None and values[1] is not None:
        startDate = get_sunrise_info - timedelta(minutes=values[0])
        endDate = get_sunrise_info + timedelta(minutes=values[1])
        time_range, snooze_check = calendar.get_event_detail(start_date, end_date, apply_snooze, snooze_days, next_day, include_free_event, title)
        
        return (time_range, snooze_check)


def sunset_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event):
    """function that return datetime of the sunrise of the input date"""
    sun_riset_info = ZipInfo(92009)

    get_sunset_info = sun_riset_info.get_sunset(next_day)
    
    if values[0] is not None and values[1] is None:

        start_date = get_sunset_info - timedelta(minutes=values[0]) - timedelta(minutes=event_duration)
        end_date = get_sunset_info - timedelta(minutes=values[0])
        time_range, snooze_check = calendar.get_event_detail(start_date, end_date, apply_snooze, snooze_days, next_day, include_free_event, title)
        
        return (time_range, snooze_check)
    
    if values[1] is not None and values[0] is None:

        start_date = get_sunset_info + timedelta(minutes=values[1])
        end_date = get_sunset_info + timedelta(minutes=values[1]) + timedelta(minutes=event_duration)
        time_range, snooze_check = calendar.get_event_detail(start_date, end_date, apply_snooze, snooze_days, next_day, include_free_event, title)
        
        return (time_range, snooze_check)

    if values[1] is not None and values[0] is not None:
        startDate = get_sunset_info - timedelta(minutes=values[0])
        endDate = get_sunset_info + timedelta(minutes=values[1])
        time_range, snooze_check = calendar.get_event_detail(start_date, end_date, apply_snooze, snooze_days, next_day, include_free_event, title)
        
        return (time_range, snooze_check)


def lowtide_filter(values, title, calendar, event_duration, apply_snooze, snooze_days, next_day, include_free_event):
    """Function that return datetime of the low tide of the input date"""
    tide_info = get_lowtide(next_day)

    if values[0] is not None and values[1] is None:
        start_date = tide_info - timedelta(minutes=lowtide1) - timedelta(minutes=event_duration)
        end_date = tide_info - timedelta(minutes=lowtide1)
        time_range, snooze_check = calendar.get_event_detail(start_date, end_date, apply_snooze, snooze_days, next_day, include_free_event, title)
        
        return (time_range, snooze_check)

    if values[1] is not None and values[0] is None:
        start_date = tide_info + timedelta(minutes=values[1])
        end_date = tide_info + timedelta(minutes=values[1]) + timedelta(minutes=event_duration)        
        time_range, snooze_check = calendar.get_event_detail(start_date, end_date, apply_snooze, snooze_days, next_day, include_free_event, title)
        
        return (time_range, snooze_check)

    if values[1] is not None and values[0] is not None:
        startDate = tide_info - timedelta(minutes=values[0])
        endDate = tide_info + timedelta(minutes=values[1])
        time_range, snooze_check = calendar.get_event_detail(start_date, end_date, apply_snooze, snooze_days, next_day, include_free_event, title)
        
        return (time_range, snooze_check)