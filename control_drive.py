#  google_api_project/control_drive.py

import os

from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient import discovery
from pprint import pprint

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

load_dotenv()

def get_list_obj(service):
    response = service.files().list(
        q='mimeType="application/vnd.google-apps.spreadsheet"')
    return response.execute()


def clear_disk(service, spreadsheets):
    for spreadsheet in spreadsheets:
        response = service.files().delete(fileId=spreadsheet['id'])
        response.execute()
