import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

def skriv_till_sheet(rad, blad_namn="Logg"):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    
    creds_dict = eval(os.environ["SERVICE_ACCOUNT_JSON"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    sheet_id = os.environ["SHEET_ID"]
    spreadsheet = client.open_by_key(sheet_id)
    blad = spreadsheet.worksheet(blad_namn)
    blad.append_row(rad)

