import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    creds = None

    if os.path.exists('token.pickle'):
        print("Loading credentials from token.pickle")
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("Refreshing expired credentials")
            creds.refresh(Request())
        else:
            print("No valid credentials available, prompting login")
            flow = InstalledAppFlow.from_client_secrets_file(
                './testbot/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        print("Saving credentials to token.pickle")
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # print("No valid credentials available, prompting login")
    # flow = InstalledAppFlow.from_client_secrets_file(
    #     './testbot/credentials.json', SCOPES)
    # creds = flow.run_local_server(port=0)
    return creds