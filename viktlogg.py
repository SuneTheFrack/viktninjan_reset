from flask import jsonify
from utils.tid import get_datum_tid
from utils.sheets import skriv_till_sheet

def _to_float(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return 0.0

def logg_vikt(data):
    # 1) datum/tid
    datum, tid = get_datum_tid(data)

    # 2) person krävs
    person = (data.get("person") or "").strip()
    if not person:
        return jsonify({"status": "error", "message": "person krävs"}), 400
    person = person.capitalize()

    # 3) värden
    vikt = _to_float(data.get("vikt"))

    # 4) bygg DICT – nycklar ska matcha kolumnnamn i 'vikt'-fliken
    rad_dict = {
        "datum": datum,
        "tid": tid,
        "person": person,
        "vikt": vikt
    }

    # 5) skriv – dict först, sedan bladnamn
    skriv_till_sheet(rad_dict, "vikt")

    # 6) svar
    return jsonify({"status": "ok", "rad": rad_dict}), 200
