from flask import request
from viktlogg import logg_vikt
from rorelselogg import logg_rorelse
from matlogg import logg_maltid_intern

def logg_allt():
    data = request.get_json()

    if not data:
        return {"status": "error", "message": "Ingen data mottagen"}, 400

    # 🧠 Är det en viktlogg?
    if "vikt" in data and data["vikt"]:
        return logg_vikt()

    # 🧠 Är det en rörelselogg?
    if "aktivitet" in data or "steg" in data or "minuter" in data:
        return logg_rorelse()

    # 🧠 Annars – vi antar att det är mat eller vätska
    return logg_maltid_intern(data)
