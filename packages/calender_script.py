from __future__ import print_function

import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def calendar_id_func(name, token_url):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(f'media/{name}_token.json'):
        creds = Credentials.from_authorized_user_file(
            f'media/{name}_token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                f'media/{token_url}', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(f'media/{name}_token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        page_token = None
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        dlist = calendar_list.get('items')
        project_ids = []
        index = 0
        while index < len(dlist):
            for key in dlist:
                ide, summary = dlist[index].get('id'), dlist[index].get('summary')
                project_ids.append((ide, summary))
                index += 1
        return project_ids
    

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    calendar_id_func()