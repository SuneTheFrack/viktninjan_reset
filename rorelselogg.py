from flask import jsonify
from gspread.exceptions import APIError
from utils.sheets import skriv_till_sheet
from utils.tid import get_datum_tid

def logg_rorelse(data):
    datum, tid = get_datum_tid(data)
    person = data.get("person", "Henrik")
    steg = data.get("steg", 0)
    rorelse_min = data.get("rorelse_min", data.get("minuter", 0))
    kalorier = data.get("kalorier", 0)

    rad = {
        "datum": datum,
        "tid": tid,
        "person": person,
        "steg": steg,
        "rorelse_min": rorelse_min,
        "kalorier": kalorier
    }

    try:
        skriv_till_sheet(rad, blad_namn="rorelse")
    except APIError:
        # Returnera kontrollerat fel utan att krascha hela appen
        return jsonify({
            "status": "error",
            "message": "Kunde inte logga rörelse – försök igen om en stund."
        }), 500

    return jsonify({
        "status": "ok",
        "message": f"✅ Rörelse loggad för {person}: {steg} steg, {rorelse_min} min, ~{kalorier} kcal."
    })
