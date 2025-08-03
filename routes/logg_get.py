from flask import request, jsonify
from utils.sheets import hamta_loggar

def las_loggar():
    """
    Flask route-funktion för att läsa loggar från Google Sheets.
    Tar emot ?person= och ?datum= som valfria query-parametrar.
    """
    person = request.args.get("person")
    datum = request.args.get("datum")

    try:
        loggar = hamta_loggar(person=person, datum=datum)
        return jsonify({"loggar": loggar}), 200
    except Exception as e:
        return jsonify({"fel": str(e)}), 500
