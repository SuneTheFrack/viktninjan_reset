from flask import jsonify
from utils.sheets import skriv_till_sheet
from utils.tid import get_datum_tid

def logg_maltid_intern(data):
datum, tid = get_datum_tid(data)
person = (data.get("person") or "").strip()
if not person:
    return jsonify({"status": "error", "message": "person krävs"}), 400
    
# valfritt – snygga till cAsE i arket:
person = person.capitalize()
print("📥 logg_maltid_intern körs")
print("🔍 inkommande data:", data)

rad = {
"datum": datum,
"tid": tid,
"person": person,
"mal": data.get("mal", ""),
"innehall": data.get("innehall", ""),
"kalorier": data.get("kalorier", 0),
"protein": data.get("protein", 0),
"fett": data.get("fett", 0),
"mattat_fett": data.get("mattat_fett", 0),
"kolhydrater": data.get("kolhydrater", 0),
"salt": data.get("salt", 0),
"fibrer": data.get("fibrer", 0),
"vatska_ml": data.get("vatska_ml", 0),
}
print("🧪 färdig rad att skriva:", rad)

skriv_till_sheet(rad, blad_namn="mat")

return jsonify({
"status": "ok",
"message": f"✅ Mat loggad för {person} kl. {tid}"
}), 200
