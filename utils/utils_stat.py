# == utils_stat.py ==

def hamta_statistik_data(person: str, manad: str) -> dict:
    # TODO: Läs från Google Sheets här.
    totals = {
        "kalorier": 0, "protein": 0, "fett": 0, "mattat_fett": 0,
        "kolhydrater": 0, "salt": 0, "fibrer": 0, "vatska_ml": 0,
        "steg": 0, "minuter": 0, "rorelse_kcal": 0
    }
    dagar = []  # t.ex. [{"datum":"2025-08-01","kalorier":123,...}]
    return {"totals": totals, "dagar": dagar}
