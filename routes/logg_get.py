from flask import request, jsonify
from utils.sheets import hamta_loggar, hamta_preferenser

def las_loggar():
    # 1) Läs parametrar
    person = request.args.get("person")
    if not person:
        return jsonify({"fel": "person saknas"}), 400

    typ   = request.args.get("typ", "all").lower()
    datum = request.args.get("datum")  # valfritt

    if typ not in ("mat", "vikt", "rorelse", "all"):
        return jsonify({"fel": f"ogiltig typ '{typ}', använd mat, vikt, rorelse eller all"}), 400

    # 2) Hämta preferenser
    try:
        pref = hamta_preferenser(person) or {}
    except Exception as e:
        return jsonify({"fel": f"fel vid preferenser: {e}"}), 500

    # 3) Statistik‐hjälpfunktioner
    def stat_mat(loggar):
        return {
            "total_kalorier":    sum(i.get("kalorier",0)   for i in loggar),
            "total_protein":     sum(i.get("protein",0)    for i in loggar),
            "total_fett":        sum(i.get("fett",0)       for i in loggar),
            "total_mattat_fett": sum(i.get("mattat_fett",0)for i in loggar),
            "total_kolhydrater": sum(i.get("kolhydrater",0)for i in loggar),
            "total_salt":        sum(i.get("salt",0)       for i in loggar),
            "total_fibrer":      sum(i.get("fibrer",0)     for i in loggar),
            "total_vatska_ml":   sum(i.get("vatska_ml",0)  for i in loggar),
        }

    def stat_vikt(loggar):
        vikter = [i.get("vikt",0) for i in loggar]
        if not vikter:
            return {"min_vikt":None, "max_vikt":None, "medel_vikt":None}
        return {
            "min_vikt":   min(vikter),
            "max_vikt":   max(vikter),
            "medel_vikt": sum(vikter)/len(vikter)
        }

    def stat_rorelse(loggar):
        return {
            "total_steg":    sum(i.get("steg",0)   for i in loggar),
            "total_minuter": sum(i.get("minuter",0)for i in loggar),
        }

    # 4) Bygg upp svar
    result = {"preferenser": pref}

    if typ == "all":
        # mat
        mat = hamta_loggar(person=person, datum=datum, typ="mat")
        result["mat"] = {"loggar": mat, "statistik": stat_mat(mat)}
        # vikt
        vikt = hamta_loggar(person=person, datum=datum, typ="vikt")
        result["vikt"] = {"loggar": vikt, "statistik": stat_vikt(vikt)}
        # rörelse
        rorelse = hamta_loggar(person=person, datum=datum, typ="rorelse")
        result["rorelse"] = {"loggar": rorelse, "statistik": stat_rorelse(rorelse)}

    else:
        loggar = hamta_loggar(person=person, datum=datum, typ=typ)
        if typ == "mat":
            statistik = stat_mat(loggar)
        elif typ == "vikt":
            statistik = stat_vikt(loggar)
        else:
            statistik = stat_rorelse(loggar)
        result["loggar"]    = loggar
        result["statistik"] = statistik

    return jsonify(result), 200
