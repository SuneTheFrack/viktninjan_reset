from flask import request, jsonify
from utils.sheets import hamta_preferenser

def las_preferenser():
    # Läs JSON-body (inte query-param). silent=True -> ingen crash om body saknas
    data = request.get_json(silent=True) or {}

    # Plocka ut "person" och trimma whitespace
    person = (data.get("person") or "").strip()

    if not person:
        # 400 Bad Request om person saknas i body
        return jsonify({"fel": "person saknas"}), 400

    # Hämta preferenserna
    data = hamta_preferenser(person)
    if not data:
        return jsonify({"fel": "person hittades inte"}), 404

    # Alltid svara JSON
    return jsonify(data), 200
