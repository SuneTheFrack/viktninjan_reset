# == route_stat.py ==

from flask import request, jsonify
from utils.utils_stat import hamta_statistik_data

def hamta_statistik():
    try:
        data = (request.get_json(silent=True) or {}) if request.method == "POST" else request.args
        person = (data.get("person") or "").strip()
        manad = (data.get("manad") or "").strip()  # YYYY-MM
        if not person or len(manad) != 7:
            return jsonify({"ok": False, "error": "person och manad (YYYY-MM) krävs"}), 400
        out = hamta_statistik_data(person, manad)
        return jsonify({"ok": True, **out}), 200
    except Exception as e:
        print(f"❌ statistik-fel: {e}")
        return jsonify({"ok": False, "error": "serverfel"}), 500
