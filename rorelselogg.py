from flask import request, jsonify
from utils.sheets import skriv_till_sheet
from utils.tid import get_datum_tid

def logg_rorelse():
    # 1) plocka JSON från request
    data = request.get_json(silent=True) or {}

    # 2) datum/tid via samma helper som matlogg använder
    datum, tid = get_datum_tid(data)

    # 3) validera person (samma krav som mat/vikt)
    person = (data.get("person") or "").strip()
    if not person:
        return jsonify({"status": "error", "message": "person krävs"}), 400
    person = person.capitalize()

    # 4) bygg rad i samma fältordning som din 'rorelse'-flik i Google Sheet
    #    (Datum, Tid, Person, Steg, Minuter, Kalorier)
    steg = int(data.get("steg", 0) or 0)
    minuter = int(data.get("minuter", 0) or 0)
    kalorier = int(data.get("kalorier", 0) or 0)

    rad = [datum, tid, person, steg, minuter, kalorier]

    # 5) skriv raden på samma sätt som matlogg skriver (men fliken heter 'rorelse')
    #    Om din matlogg inte använder 'append_row', ersätt raden nedan med motsvarande anrop.
    append_row("rorelse", rad)

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
