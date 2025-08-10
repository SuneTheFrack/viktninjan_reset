from flask import request, jsonify
from utils.tid import get_datum_tid
from utils.sheets import skriv_till_sheet

def _to_int(v):
    try:
        return int(v)
    except (TypeError, ValueError):
        return 0

def logg_rorelse_intern(data):
    # 1) datum/tid
    datum, tid = get_datum_tid(data)

    # 2) person krävs
    person = (data.get("person") or "").strip()
    if not person:
        return jsonify({"status": "error", "message": "person krävs"}), 400
    person = person.capitalize()

    # 3) fält (robust konvertering)
    steg = _to_int(data.get("steg"))
    minuter = _to_int(data.get("minuter"))
    kalorier = _to_int(data.get("kalorier"))

    # 4) bygg DICT – nycklar måste matcha kolumnnamn i 'rorelse'-fliken
    rad_dict = {
        "datum": datum,
        "tid": tid,
        "person": person,
        "steg": steg,
        "minuter": minuter,
        "kalorier": kalorier,
    }

    # 5) skriv – dict först, sedan bladnamn
    skriv_till_sheet(rad_dict, "rorelse")

    # 6) svar
    return jsonify({"status": "ok", "rad": rad_dict}), 200

# Flask-view: plocka JSON och kalla intern-funktionen
def logg_rorelse():
    data = request.get_json(silent=True) or {}
    return logg_rorelse_intern(data)
