from googleapiclient.discovery import build
from google.oauth2 import service_account

def append_data_to_sheet(id, name, age, email, phone):
    SERVICE_ACCOUNT_FILE = 'keys.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )

    SAMPLE_SPREADSHEET_ID = '1AFdzxOfXrL0WBXFpFoswP7-sR1s88qM1ffQpuvbFlF9c'

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()

    resource = {
        "values": [[id, name, age, email, phone]]
    }

    sheet.values().append(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range="table1!A1",
        valueInputOption="USER_ENTERED",
        body=resource
    ).execute()