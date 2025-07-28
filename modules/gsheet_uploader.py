import gspread
from oauth2client.service_account import ServiceAccountCredentials

def upload_to_google_sheet(col, sheet_name="MPCH case List"):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds/credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open(sheet_name).sheet1
    sheet.update('G2', col)  # Skip header row
