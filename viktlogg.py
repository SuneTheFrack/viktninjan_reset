from flask import request, jsonify
import datetime
from utils.sheets import skriv_till_sheet  # För att skriva till Google Sheet

def logg_vikt():
    data = request.get_json()

    if not data or "vikt" not in data:
        return jsonify({"status": "error", "message": "Ingen vikt angiven"}), 400

    vikt = data["vikt"]
    datum = data.get("datum") or datetime.date.today().isoformat()
    tid = data.get("tid") or datetime.datetime.now().strftime("%H:%M")
    person = data.get("person", "Henrik")

    # Bygg raden som ska skrivas in i Google Sheet-bladet "Vikt"
    rad = [datum, tid, person, vikt]

    # 📝 Viktigt: blad_namn = "Vikt" (inte "Viktlogg" som tidigare!)
    skriv_till_sheet(rad, blad_namn="Vikt")

    return jsonify({
        "status": "ok",
        "message": f"✅ Vikt {vikt} kg loggad för {person} kl. {tid}"
    }), 200
