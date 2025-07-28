import gspread
from oauth2client.service_account import ServiceAccountCredentials

def read_links_from_column_j(sheet_name="MPCH case List"):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds/credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open(sheet_name).sheet1

    # Get all values in column J (10th column), skipping header
    links = sheet.col_values(10)[1:]  # [1:] skips the header row (row 1)

    # Optional: filter out empty cells
    links = [link for link in links if link.strip()]

    return links
