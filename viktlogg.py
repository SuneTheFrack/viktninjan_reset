from flask import jsonify

def logg_vikt(data):
    datum, tid = get_datum_tid(data)

    person = (data.get("person") or "").strip()
    if not person:
        return jsonify({"status": "error", "message": "person krävs"}), 400
    person = person.capitalize()

    print("📥 logg_vikt körs")
    print("🔍 inkommande data:", data)

    rad = {
        "datum": datum,
        "tid": tid,
        "person": person,
        "vikt": data.get("vikt", 0)
    }

    # TODO: skriv rad till Google Sheet här...
    return jsonify({"status": "ok", "rad": rad}), 200
