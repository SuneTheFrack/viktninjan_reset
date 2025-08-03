from flask import request, jsonify
from utils.sheets import hamta_preferenser

def las_preferenser():
    person = request.args.get("person")
    if not person:
        return jsonify({"fel": "person saknas"}), 400

    data = hamta_preferenser(person)
    if not data:
        return jsonify({"fel": "person hittades inte"}), 404

    return jsonify(data), 200
