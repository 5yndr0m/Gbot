#pip install google-api-python-client
import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
PARENT_FOLDER_ID = os.getenv('PARENT_FOLDER_ID')

def authenticate():
    creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

def upload_fun(file_path):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_name = os.path.basename(file_path)

    file_metadata = {
        'name' : file_name,
        'parents' : [PARENT_FOLDER_ID]
    }

    media = MediaFileUpload(file_path, resumable=True)

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    # print(f'File ID: {file.get("id")}')

if __name__ == "__main__":
    upload_fun("./testbot/unnamed.png")

