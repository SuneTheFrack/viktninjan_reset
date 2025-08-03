# utils.py
# Hjälpfunktioner för loggmoduler

from datetime import datetime
from zoneinfo import ZoneInfo


def get_datum_tid(data):
    now = datetime.now(ZoneInfo("Europe/Stockholm"))

    datum = data.get("datum")
    if not datum or str(datum).strip().lower() == "nu":
        datum = now.strftime("%Y-%m-%d")

    tid = data.get("tid")
    if not tid or str(tid).strip().lower() == "nu":
        tid = now.strftime("%H:%M")

    return datum, tid

