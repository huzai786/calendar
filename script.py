import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calen.settings')
django.setup()


from cal.models import EventDetails
from script_func import main_func

from datetime import datetime
from packages.script_utils import get_event_duration, get_snooze_duration, add_msg




def script():
    date = datetime.now().strftime('%m-%d-%Y.%I%p.%Mmin%Ssec')
    msg = ''
    for event in EventDetails.objects.all():
        
        title = event.title
        
        days_to_look = event.days_to_look
        
        days = list(event.days)
        
        filter_data = [{'filter_name': filter.keyword, 'x1': filter.X1, 'x2': filter.X2, 'filter_detail': filter.filter_detail} for filter in event.filter.all()]
        include_free_event = event.free_event

        event_duration = get_event_duration(
            event.event_duration, event.event_duration_type)
        
        snooze_duration = get_snooze_duration(
            event.snooze_duration, event.snooze_type)
        
        apply_snooze = event.apply_snooze
        snooze_days = list(event.snooze_days)
        
        calender_ids = [{'name': i.name, 'id': i.ide,
                        'token_url': i.token_url, 'title': i.title} for i in event.calenders.all()]

        mesg = main_func(title, days_to_look, calender_ids, days, filter_data, event_duration, \
                        snooze_duration, apply_snooze, snooze_days, include_free_event)
        msg += mesg

    add_msg(date, msg)



if __name__ == '__main__':
    script()