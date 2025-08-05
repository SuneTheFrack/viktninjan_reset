from flask import request, jsonify
from utils.tid import get_datum_tid
from utils.sheets import skriv_till_sheet

def logg_vikt():
    data = request.get_json()
    print("📥 logg_vikt körs")
    print("📦 JSON från GPT:", data)

    # Hämta datum och tid (inklusive "nu")
    datum, tid = get_datum_tid(data)

    # Validera person
    person = data.get("person", "")
    if not person:
        return jsonify({"status": "error", "message": "Person saknas"}), 400

    # Validera vikt
    vikt = data.get("vikt")
    if vikt is None:
        return jsonify({"status": "error", "message": "Vikt saknas"}), 400

    # Bygg upp raden
    rad = {
        "datum": datum,
        "tid": tid,
        "person": person,
        "vikt": vikt,
        "muskelvikt": data.get("muskelvikt", 0),
        "fettprocent": data.get("fettprocent", 0),
        "vattenprocent": data.get("vattenprocent", 0),
        "bmr": data.get("bmr", 0),
    }
    print("🧪 färdig rad att skriva (vikt):", rad)

    # Skriv till rätt flik i ditt Google Sheet
    skriv_till_sheet(rad, blad_namn="vikt")

    # Skicka bekräftelse tillbaka
    return jsonify({
        "status": "ok",
        "message": f"✅ Vikt loggad för {person}: {vikt} kg"
    }), 200
