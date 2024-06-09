#pip install google-api-python-client python-dotenv
import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from dotenv import load_dotenv
from authenticate import authenticate

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/drive']
PARENT_FOLDER_ID = os.getenv('PARENT_FOLDER_ID')

# def authenticate():
#     print("No valid credentials available, prompting login")
#     flow = InstalledAppFlow.from_client_secrets_file(
#         './testbot/credentials.json', SCOPES)
#     creds = flow.run_local_server(port=0)
#     return creds

def upload_fun(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_name = os.path.basename(file_path)

    file_metadata = {
        'name': file_name,
        'parents': [PARENT_FOLDER_ID]
    }

    media = MediaFileUpload(file_path, resumable=True)

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f'File ID: {file.get("id")}')

if __name__ == "__main__":
    upload_fun("./testbot/unnamed.png")
