from __future__ import print_function

import os.path
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pytz
import sys
from datetime import datetime 


class CalendarEvent(object):

    def __init__(self, name, token_url, calender_id):
        self.SCOPES = ['https://www.googleapis.com/auth/calendar'] 
        self.name = name
        self.token_url = token_url 
        self.calender_id = calender_id 

    def get_event_detail(self, start_date, end_date, apply_snooze, snooze_days, next_day, include_free_event, title):
        creds = None
        path = f'media/{self.name}_token.json'
        if os.path.exists(path):
            creds = Credentials.from_authorized_user_file(path, self.SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                except Exception as e:
                    os.remove(path)
                    sys.exit()
                    
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    f'media/{self.token_url}', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open(f'media/{self.name}_token.json', 'w') as token:
                token.write(creds.to_json())
        page_token = None
        service = build('calendar', 'v3', credentials=creds)
        myTimeZone = pytz.timezone('US/Pacific')
        start = myTimeZone.localize(start_date)
        end = myTimeZone.localize(end_date)

        try:
            events = service.events().list(calendarId=self.calender_id, pageToken=page_token, timeMin= start.isoformat(), timeMax = end.isoformat()).execute()
            print(len(events['items']))
            if len(events['items']) > 0:
                event_ids = [event['id'] for event in events['items']]
                event_names = [event['summary'] for event in events['items']]
                if apply_snooze:
                    if len(snooze_days) > 0:
                        if next_day.strftime('%A') in snooze_days:
                            if title in event_names:
                                return None, True
                    else:
                        if title in event_names:
                            return None, True
                free_date_ranges = []
                busy_date_ranges = []
                free_event_names = []
                busy_event_names = []
                for e in event_ids:
                    single_event = service.events().get(calendarId=self.calender_id, eventId=e).execute()
                    event_name = single_event['summary']
                    if not single_event['start'].get('dateTime'):
                        return None, False
                    if single_event['start'].get('dateTime') and single_event['end'].get('dateTime'):
                        x = datetime.strptime(single_event['start'].get('dateTime'), '%Y-%m-%dT%H:%M:%S%z').replace(tzinfo = None)
                        y = datetime.strptime(single_event['end'].get('dateTime'), '%Y-%m-%dT%H:%M:%S%z').replace(tzinfo = None)
                        x = datetime.combine(start_date.date(), x.time())
                        y = datetime.combine(end_date.date(), y.time()) 
                    if 'transparency' not in single_event:
                        busy_date_ranges.append((x, y))
                        busy_event_names.append(event_name)
                    
                    if 'transparency' in single_event:
                        free_date_ranges.append((x, y))
                        free_event_names.append(event_name)
                        
                if include_free_event is True:
                    date_range = free_date_ranges + busy_date_ranges
                    event_names = free_event_names + busy_event_names
                    return list(set(sorted(date_range))), False
                if include_free_event is False:
                    return list(set(sorted(busy_date_ranges))), False
            else:
                return [(start_date, end_date)], False
            
        except Exception as e:
            print('error: ', e)



