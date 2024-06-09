import os
import pickle
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from dotenv import load_dotenv
from authenticate import authenticate

def list_files(folder_id=None):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    if folder_id:
        query = f"'{folder_id}' in parents"
    else:
        query = "'root' in parents"

    results = service.files().list(
        q=query,
        pageSize = 10,
        fields = "nextPageToken, files(id, name)"
    ).execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(f'{item["name"]}')
    
def create_folder(folder_name):
    #add a way to get current working dir
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }

    folder = service.files().create(
        body=file_metadata,
        fields='id'
    ).execute()
    print(f'Folder ID: {folder.get("id")}')

def navigate_to(folder_name):
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'"
    response = service.files().list(
        q=query,
        pageSize=1
    ).execute()
    folders = response.get('files', [])
    if not folders:
        print(f'Folder "{folder_name}" not found.')
        return None
    else:
        folder_id = folders[0]['id']
        print(f'Navigating to folder "{folder_name}"')
        return folder_id

def navigate_back():
    previous_folder_id = '<previous_folder_id>'
    if previous_folder_id:
        print(f'Navigating back to previous folder')
        return previous_folder_id
    else:
        print('No previous folder to navigate back to.')
        return None

if __name__ == "__main__":
    list_files()
    folder_name = input('Enter folder name:')
    folder_id = navigate_to(folder_name)

    if folder_id:
        list_files(folder_id)

    navigate_back()

    list_files()
