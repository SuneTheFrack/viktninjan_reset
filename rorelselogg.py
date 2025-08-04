# rorelselogg.py
# Tar emot rörelsedata och loggar det till fliken "Rorelse" i Google Sheets

from flask import request, jsonify
from tidutils import get_datum_tid
from utils.sheets import skriv_till_sheet

def logg_rorelse():
    data = request.json

    # Hämtar datum och tid, inklusive stöd för "nu"
    datum, tid = get_datum_tid(data)

    rad = {
        "datum": datum,
        "tid": tid,
        "person": data.get("person"),
        "steg": data.get("steg", ""),
        "rorelsetid_min": data.get("rorelsetid_min", ""),
        "kalorier": data.get("kalorier", "")
    }

    skriv_till_sheet(rad, blad_namn="rorelse")

    return jsonify({
        "status": "ok",
        "message": f"🏃 Rörelse loggad för {rad['person']}"
    }), 200
