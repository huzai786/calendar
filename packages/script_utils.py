#  UTILITIES

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



def findFirstOpenSlot(date_ranges, startTime, endTime, duration, event_names, title, snooze_check, snooze_days, start_date):
    if date_ranges is not None:
        date_ranges = sorted(date_ranges)
        print('date_ranges', date_ranges)
        eventStarts = [i[0] for i in date_ranges]
        eventEnds = [i[1] for i in date_ranges]
        firstEvent = eventStarts[0]
        lastEvent = eventEnds[-1]
        print('startTime', startTime)
        print('firstEvent', firstEvent)
        print(firstEvent - startTime)
        can_be = []                
        not_be = []
        possible_dates = []
        print(event_names)
        for i, v in enumerate(zip(eventStarts[1:], eventEnds[:-1])):
            if v[0] > v[1]:
                gap = v[0] - v[1]
                if duration < gap:
                    can_be.append(v[1])
            else:
                not_be.append(v[1])
        for i, v in enumerate(can_be):
            if any(v > x for x in not_be):
                possible_dates.append(v)
                
        if duration < (firstEvent - startTime):
            return startTime, False
        
        if len(possible_dates) != 0:
            return possible_dates[0], False
        
        if duration < (endTime - lastEvent):
            return lastEvent, False
        
        if snooze_check is True:
            if snooze_days == []:
                if title in event_names:
                    return None, True
                else:
                    return None, False  
                
            if snooze_days != []:
                if title in event_names and (start_date.strftime('%A') in snooze_days):
                    return None, True
                else:
                    return None, False
        else:
            print('end part')
            return None, False 
    else:
        return startTime, False
