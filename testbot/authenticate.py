from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    print("No valid credentials available, prompting login")
    flow = InstalledAppFlow.from_client_secrets_file(
        './testbot/credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return creds