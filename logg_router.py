from flask import request
from viktlogg import logg_vikt
from rorelselogg import logg_rorelse
from matlogg import logg_maltid_intern

def logg_allt():
    data = request.get_json()
    print("📥 /logg kallad")
    print("📦 JSON från GPT:", data)

    if "vikt" in data and data["vikt"]:
        print("📌 Det är en viktlogg")
        return logg_vikt()

    if "aktivitet" in data or "steg" in data or "minuter" in data:
        print("📌 Det är en rörelselogg")
        return logg_rorelse()

    print("📌 Det är en matlogg – skickar till logg_maltid_intern")
    return logg_maltid_intern(data)
