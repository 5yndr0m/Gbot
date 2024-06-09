import os
import io
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = os.getenv('SERVICE_ACCOUNT_FILE')
PARENT_FOLDER_ID = os.getenv('PARENT_FOLDER_ID')

def authenticate():
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return creds

def download_file(file_id, file_name):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    request = service.files().get_media(fileId=file_id)
    file_path = os.path.join(os.getcwd(), file_name)

    with io.FileIO(file_path, 'wb') as file_handle:
        downloader = MediaIoBaseDownload(file_handle, request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%.")

    print(f'File downloaded to {file_path}')

file_id = 'your-file-id'
folder_name = 'New Folder'

download_file(file_id, file_name)