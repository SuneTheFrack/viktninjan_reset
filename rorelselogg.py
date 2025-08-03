# rorelselogg.py
# Tar emot rörelsedata och loggar det till fliken "Rorelse" i Google Sheets

from flask import request, jsonify
from auth import sheet
from tidutils import get_datum_tid

def logg_rorelse():
    data = request.json

    # Hämtar datum och tid, inklusive stöd för "nu"
    datum, tid = get_datum_tid(data)

    row = [
        datum,
        tid,
        data.get("person", ""),
        data.get("steg", ""),
        data.get("rorelsetid_min", ""),
        data.get("kalorier", "")
    ]

    sheet.worksheet("Rorelse").append_row(row)
    return jsonify({"status": "OK", "rad": row}), 200
