import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calen.settings')
django.setup()


from cal.models import EventDetails
from script_func import main_func

from datetime import datetime
from packages.script_utils import get_event_duration, get_snooze_duration, add_msg




def script():
    date = datetime.now().strftime('%m-%d-%Y_%I_%p_%M_%S')
    print(date)
    msg = ''
    for event in EventDetails.objects.all():
        
        title = event.title
        
        days_to_look = event.days_to_look
                
        days = list(event.days)
        
        filter_data = [{'filter_name': filter.keyword, 'x1': filter.X1, 'x2': filter.X2, 'temperature_included': filter.add_temperature, 
                        'tempX1':filter.Temperature_X1, 'tempX2': filter.Temperature_X2,
                        'filter_detail': filter.filter_detail} for filter in event.filter.all()]
        
        event_duration = get_event_duration(
            event.event_duration, event.event_duration_type)
        
        snooze_duration = get_snooze_duration(
            event.snooze_duration, event.snooze_type)
        
        apply_snooze = event.apply_snooze
        snooze_days = list(event.snooze_days)
        
        calender_ids = [{'name': i.name, 'id': i.ide,
                        'token_url': i.token_url, 'title': i.title} for i in event.calenders.all()]

        mesg = main_func(title, days_to_look, calender_ids, days, filter_data, event_duration, \
                        snooze_duration, apply_snooze, snooze_days)
        msg += mesg

    add_msg(date, msg)



if __name__ == '__main__':
    script()