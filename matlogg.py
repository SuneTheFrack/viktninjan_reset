from flask import jsonify
from utils.tid import get_datum_tid            # samma helper som tidigare
from utils.sheets import skriv_till_sheet      # samma skriv-funktion som tidigare

def _to_float(v):
    try:
        # tillåt "85", "85.0" osv
        return float(v)
    except (TypeError, ValueError):
        return 0.0

def logg_maltid_intern(data):
    # 1) datum/tid
    datum, tid = get_datum_tid(data)

    # 2) person krävs
    person = (data.get("person") or "").strip()
    if not person:
        return jsonify({"status": "error", "message": "person krävs"}), 400
    person = person.capitalize()

    # 3) plocka fält (alla ska finnas – fyll med 0/"" om saknas)
    mal = (data.get("mal") or "").strip()
    innehall = (data.get("innehall") or "").strip()
    kalorier = _to_float(data.get("kalorier"))
    protein = _to_float(data.get("protein"))
    fett = _to_float(data.get("fett"))
    mattat_fett = _to_float(data.get("mattat_fett"))
    kolhydrater = _to_float(data.get("kolhydrater"))
    salt = _to_float(data.get("salt"))
    fibrer = _to_float(data.get("fibrer"))
    vatska_ml = _to_float(data.get("vatska_ml"))

    # 4) bygg rad i exakt samma kolumnordning som "mat"-arket
    #    [datum, tid, person, mal, innehall, kalorier, protein, fett, mattat_fett, kolhydrater, salt, fibrer, vatska_ml]
    rad_dict = [
        datum, tid, person, mal, innehall,
        kalorier, protein, fett, mattat_fett,
        kolhydrater, salt, fibrer, vatska_ml
    ]

    # 5) skriv raden
    skriv_till_sheet(rad_dict, "mat")

    # 6) svar
    return jsonify({
        "status": "ok",
        "rad": {
            "datum": datum,
            "tid": tid,
            "person": person,
            "mal": mal,
            "innehall": innehall,
            "kalorier": kalorier,
            "protein": protein,
            "fett": fett,
            "mattat_fett": mattat_fett,
            "kolhydrater": kolhydrater,
            "salt": salt,
            "fibrer": fibrer,
            "vatska_ml": vatska_ml
        }
    }), 200
