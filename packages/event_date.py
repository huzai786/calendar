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

    def calendar_event_func(self, startDate, endDate, include_free_event):
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
        # Save the credentials for the next run
            with open(f'media/{self.name}_token.json', 'w') as token:
                token.write(creds.to_json()) 
        page_token = None
        service = build('calendar', 'v3', credentials=creds)
        myTimeZone = pytz.timezone('US/Pacific')
        start = myTimeZone.localize(startDate)
        end = myTimeZone.localize(endDate)
        try:
            events = service.events().list(calendarId=self.calender_id, pageToken=page_token, timeMax = end.isoformat(), timeMin= start.isoformat()).execute()
            events = [(event['summary']) for event in events['items']]
            event_ids = [(event['id']) for event in events['items']]
            
            if len(events) != 0:
                free_event_names = []
                busy_event_names = []
                for e in event_ids:
                    event = service.events().get(calendarId=self.calender_id, eventId=e).execute()
                    
                    if not event['start'].get('dateTime'):
                        return True, [event['summary']]

                    if 'transparency' not in event:
                        busy_event_names.append(event['summary'])

                    if 'transparency' in event:
                        free_event_names.append(event['summary'])

                if include_free_event is True:
                    event_names = free_event_names + busy_event_names
                    if len(event_names) != 0:
                        return True, event_names

                    else:
                        return None, []

                if include_free_event is False:
                    if len(busy_event_names) != 0:
                        return True, busy_event_names

                    else:
                        return None, []

            return None, []

        except Exception as e:
            print('error: ', e)

    def get_event_detail(self, startDate, endDate, include_free_event):
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
        # Save the credentials for the next run
            with open(f'media/{self.name}_token.json', 'w') as token:
                token.write(creds.to_json()) 
        
        page_token = None
        service = build('calendar', 'v3', credentials=creds)
        myTimeZone = pytz.timezone('US/Pacific')
        start = myTimeZone.localize(startDate)
        end = myTimeZone.localize(endDate)

        try:
            events = service.events().list(calendarId=self.calender_id, pageToken=page_token, timeMax = end.isoformat(), timeMin= start.isoformat()).execute()
            events = [event['id'] for event in events['items']]
            if len(events) != 0:
                free_date_ranges = []
                busy_date_ranges = []
                free_event_names = []
                busy_event_names = []
                for e in events:
                    event = service.events().get(calendarId=self.calender_id, eventId=e).execute()
                    event_name = event['summary']

                    if not event['start'].get('dateTime'):
                        return [(startDate, endDate)], [event_name]

                    if event['start'].get('dateTime') and event['end'].get('dateTime'):
                        x = datetime.strptime(event['start'].get('dateTime'), '%Y-%m-%dT%H:%M:%S%z').replace(tzinfo = None)
                        y = datetime.strptime(event['end'].get('dateTime'), '%Y-%m-%dT%H:%M:%S%z').replace(tzinfo = None)

                        xi = datetime.combine(startDate.date(), x.time())
                        yi = datetime.combine(endDate.date(), y.time()) 


                    if 'transparency' not in event:

                        busy_date_ranges.append((xi, yi))
                        busy_event_names.append(event_name)
                    
                    if 'transparency' in event:

                        free_date_ranges.append((xi, yi))
                        free_event_names.append(event_name)
                        
                if include_free_event is True:

                    date_range = free_date_ranges + busy_date_ranges
                    event_names = free_event_names + busy_event_names
                    return list(set(sorted(date_range))), event_names

                if include_free_event is False:
                    return list(set(sorted(busy_date_ranges))), busy_event_names
            else:
                return (None, [])
            
        except Exception as e:
            print('error: ', e)



