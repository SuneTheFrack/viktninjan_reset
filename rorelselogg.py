from flask import request, jsonify

def logg_rorelse():
    # plocka JSON från request-body
    data = request.get_json(silent=True) or {}

    # datum/tid enligt din hjälpfunktion
    datum, tid = get_datum_tid(data)

    # person krävs
    person = (data.get("person") or "").strip()
    if not person:
        return jsonify({"status": "error", "message": "person krävs"}), 400
    person = person.capitalize()

    print("📥 logg_rorelse körs")
    print("🔍 inkommande data:", data)

    rad = {
        "datum": datum,
        "tid": tid,
        "person": person,
        "steg": data.get("steg", 0),
        "minuter": data.get("minuter", 0),
        "kalorier": data.get("kalorier", 0),
    }

    # TODO: skriv rad till Google Sheet här (samma som tidigare)
    return jsonify({"status": "ok", "rad": rad}), 200
