import gspread
import os
import json
from oauth2client.service_account import ServiceAccountCredentials

# == ge rättigheter att läsa och skriva ==
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# == skriv till sheet ==
def skriv_till_sheet(rad, blad_namn="Logg"):
    
    import json  # lägg detta högst upp om det inte finns
    creds_dict = json.loads(os.environ["SERVICE_ACCOUNT_JSON"])

    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    sheet_id = os.environ["SHEET_ID"]
    spreadsheet = client.open_by_key(sheet_id)
    blad = spreadsheet.worksheet(blad_namn)
    blad.append_row(rad)

# == läs från sheet ==
def hamta_loggar(blad_namn="Logg", person=None, datum=None):
    creds_dict = json.loads(os.environ["SERVICE_ACCOUNT_JSON"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(os.environ["SHEET_ID"])
    blad = spreadsheet.worksheet(blad_namn)
    rader = blad.get_all_records()

    filtrerade = []
    for rad in rader:
        if person and rad["person"].lower() != person.lower():
            continue
        if datum and rad["datum"] != datum:
            continue
        filtrerade.append(rad)

    return filtrerade
