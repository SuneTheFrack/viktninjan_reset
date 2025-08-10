from flask import request, jsonify
from utils.tid import get_datum_tid            # samma helper som i matlogg
from utils.sheets import skriv_till_sheet      # samma skriv-funktion som i matlogg

def _to_int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return 0

def logg_rorelse_intern(data):
    # 1) datum/tid via samma helper som matlogg
    datum, tid = get_datum_tid(data)

    # 2) person krävs (samma validering som mat/vikt)
    person = (data.get("person") or "").strip()
    if not person:
        return jsonify({"status": "error", "message": "person krävs"}), 400
    person = person.capitalize()

    # 3) plocka fält (robust int-konvertering)
    steg = _to_int(data.get("steg"))
    minuter = _to_int(data.get("minuter"))
    kalorier = _to_int(data.get("kalorier"))

    # 4) bygg rad i samma ordning som 'rorelse'-fliken i Google Sheet
    rad = [datum, tid, person, steg, minuter, kalorier]

    # 5) skriv till sheet – exakt samma funktion som matlogg använder
    skriv_till_sheet("rorelse", rad)

    # 6) svar
    return jsonify({
        "status": "ok",
        "rad": {
            "datum": datum,
            "tid": tid,
            "person": person,
            "steg": steg,
            "minuter": minuter,
            "kalorier": kalorier
        }
    }), 200

# Tunn Flask-view som matchar mönstret i matlogg: plocka JSON och kalla intern-funktionen
def logg_rorelse():
    data = request.get_json(silent=True) or {}
    return logg_rorelse_intern(data)
