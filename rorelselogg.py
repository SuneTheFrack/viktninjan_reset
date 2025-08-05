# rorelselogg.py
from flask import request, jsonify
from utils.tid import get_datum_tid
from utils.sheets import skriv_till_sheet

def logg_rorelse():
    data = request.get_json()
    print("📥 logg_rorelse körs")
    print("🔍 inkommande data:", data)

    # 1) Datum & tid
    datum, tid = get_datum_tid(data)

    # 2) Validera person
    person = data.get("person", "")
    if not person:
        return jsonify({"status": "error", "message": "Person saknas"}), 400

    # 3) Hämta rörelsedata (default 0)
    steg      = data.get("steg", 0)
    minuter   = data.get("minuter", 0)
    kalorier  = data.get("kalorier", 0)

    # 4) Bygg rad-dict
    rad = {
        "datum": datum,
        "tid": tid,
        "person": person,
        "steg": steg,
        "minuter": minuter,
        "kalorier": kalorier
    }
    print("🧪 färdig rad att skriva (rorelse):", rad)

    # 5) Skriv till fliken "rorelse"
    skriv_till_sheet(rad, blad_namn="rorelse")

    # 6) Svara
    return jsonify({
        "status": "ok",
        "message": f"✅ Rörelse loggad för {person}: {steg} steg, {minuter} min, ~{kalorier} kcal"
    }), 200
