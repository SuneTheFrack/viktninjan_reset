import gspread
import os
import json
from oauth2client.service_account import ServiceAccountCredentials

# == ge rättigheter att läsa och skriva ==
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# == skriv till sheet ==
import gspread
import os
import json
import time
from oauth2client.service_account import ServiceAccountCredentials
from gspread.exceptions import APIError

# == ge rättigheter att läsa och skriva ==
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

# == skriv till sheet ==
def skriv_till_sheet(rad_dict, blad_namn="mat"):
    print(f"📤 skriver till blad: {blad_namn}")
    print("🧾 data att logga (dict):", rad_dict)

    # Autentisering
    creds_dict = json.loads(os.environ["SERVICE_ACCOUNT_JSON"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    # Öppna Google Sheet och blad
    sheet_id = os.environ["SHEET_ID"]
    spreadsheet = client.open_by_key(sheet_id)

    try:
        blad = spreadsheet.worksheet(blad_namn)
    except gspread.exceptions.WorksheetNotFound:
        print(f"❌ Hittar inte bladet '{blad_namn}' – kontrollera fliknamnet i Google Sheet!")
        raise

    # Hämta kolumnrubriker från första raden och gör dem lowercase
    kolumnnamn = [k.lower() for k in blad.row_values(1)]

    # Skapa en rad i rätt ordning, fyll tomma med ""
    rad = [rad_dict.get(k, "") for k in kolumnnamn]
    print("✅ färdig rad att skriva (lista):", rad)

    # Försök append med retry
    max_retries = 3
    for attempt in range(1, max_retries + 1):
        try:
            blad.append_row(rad)
            print(f"✅ append lyckades på försök {attempt}")
            return
        except APIError as e:
            print(f"⚠️ APIError vid append (försök {attempt}/{max_retries}): {e}")
            if attempt < max_retries:
                time.sleep(1)  # vänta en sekund innan nästa försök
            else:
                print("❌ Ger upp – kunde inte skriva till sheet")
                # Lyft felet så att din route kan returnera ett kontrollerat 500-svar
                raise


# == läs loggar från sheet ==
def hamta_loggar(person=None, datum=None, typ="mat"):
    blad_namn = {
        "mat": "mat",
        "rorelse": "rorelse",
        "vikt": "vikt"
    }.get(typ.lower(), "mat")

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

# == läs preferenser från sheet ==
def hamta_preferenser(person):
    creds_dict = json.loads(os.environ["SERVICE_ACCOUNT_JSON"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key(os.environ["SHEET_ID"])
    blad = spreadsheet.worksheet("preferenser")
    rader = blad.get_all_records()

    for rad in rader:
        if rad["person"].lower() == person.lower():
            return rad
    return None

# == hämta kolumnnamn från ett blad ==
def hamta_kolumnnamn(blad_namn):
    creds_dict = json.loads(os.environ["SERVICE_ACCOUNT_JSON"])
    creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
    client = gspread.authorize(creds)

    sheet_id = os.environ["SHEET_ID"]
    spreadsheet = client.open_by_key(sheet_id)
    blad = spreadsheet.worksheet(blad_namn)

    kolumnnamn = blad.row_values(1)
    return [k.lower() for k in kolumnnamn]
