from __future__ import print_function

import os.path
import os
from pytz import timezone
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pytz
import sys
import pprint


class CalendarEvent(object):

    def __init__(self, name, token_url, calender_id):
        self.SCOPES = ['https://www.googleapis.com/auth/calendar'] 
        self.name = name
        self.token_url = token_url 
        self.calender_id = calender_id 

    def calendar_event_func(self, startDate, endDate):
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
            events = [(event['summary'], events['id']) for event in events['items']]
            
            if len(events) != 0:
                return (True, events)
            else:
                return (None, [])
        except Exception as e:
            print(e)

    def get_event_detail(self, event_id):
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
        service = build('calendar', 'v3', credentials=creds)
        try:
            event = service.events().get(calendarId=self.calender_id, eventId=event_id).execute()
            with open('data.txt', 'w', encoding='utf-8') as f:
                f.write(pprint.pformat(events))            
        except Exception as e:
            print('error: ', e)




