from datetime import datetime

def get_datum_tid(data):
    datum = data.get("datum")
    tid = data.get("tid")

    if not datum or datum == "nu":
        datum = datetime.now().strftime("%Y-%m-%d")

    if not tid or tid == "nu":
        tid = datetime.now().strftime("%H:%M")

    return datum, tid
