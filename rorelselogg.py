# rorelselogg.py 
# Tar emot rörelsedata och loggar det till fliken "Rorelse" i Google Sheets

from flask import request, jsonify
from utils.tid import get_datum_tid
from utils.sheets import skriv_till_sheet
from gspread.exceptions import APIError

def logg_rorelse():
# 1) Läs in data och debug-logg
data = request.get_json()
print("📥 logg_rorelse körs")
print("🔍 inkommande data:", data)

# 2) Datum & tid (stöd för "nu")
datum, tid = get_datum_tid(data)

# 3) Validera person
person = data.get("person", "")
if not person:
return jsonify({"status": "error", "message": "Person saknas"}), 400

# 4) Hämta rörelsedata (default 0), stöd både "minuter" och "rorelsetid_min"
steg         = data.get("steg", 0)
rorelse_min  = data.get("rorelsetid_min", data.get("minuter", 0))
kalorier     = data.get("kalorier", 0)

# 5) Bygg rad-dict i exakt samma kolumnordning
rad = {
"datum": datum,
"tid": tid,
"person": person,
"steg": steg,
        "rorelsetid_min": rorelse_min,
        "minuter": rorelse_min,
"kalorier": kalorier
}
print("🧪 färdig rad att skriva (rorelse):", rad)

# 6) Skriv till Google Sheet med retry och felhantering
try:
skriv_till_sheet(rad, blad_namn="rorelse")
except APIError as e:
print("❌ Kunde inte logga rörelse (APIError):", e)
return jsonify({
"status": "error",
"message": "Kunde inte logga rörelse – försök igen om en stund."
}), 500

# 7) Returnera framgång
return jsonify({
"status": "ok",
"message": f"✅ Rörelse loggad för {person}: {steg} steg, {rorelse_min} min, ~{kalorier} kcal"
}), 200
