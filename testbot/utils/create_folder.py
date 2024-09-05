import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from authenticate import authenticate


def create_folder(folder_name):
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

folder_name = 'New Folder'

create_folder(folder_name)