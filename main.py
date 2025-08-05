from flask import Flask
from logg_router import logg_allt
from routes.logg_get import las_loggar
from viktlogg import logg_vikt
from rorelselogg import logg_rorelse
from routes.preferenser import las_preferenser

print("✅ Flask och imports klara")

app = Flask(__name__)
print("✅ Flask-app initierad")

# POST /logg → logga mat, vikt eller rörelse
app.add_url_rule("/logg", view_func=logg_allt, methods=["POST"])
print("✅ /logg (POST) registrerad")

# GET /logg → hämta loggar (mat, vikt, rörelse eller all)
app.add_url_rule("/logg", view_func=las_loggar, methods=["GET"])
print("✅ /logg (GET) registrerad")

# POST /loggvikt → separat vikt-endpoint (om ni vill)
app.add_url_rule("/loggrorelse", view_func=logg_rorelse, methods=["POST"])
print("✅ /loggrorelse registrerad")


# POST /loggrorelse → separat rörelse-endpoint (om ni vill)
app.add_url_rule("/loggrorelse", view_func=logg_rorelse, methods=["POST"])
print("✅ /loggrorelse registrerad")


# GET /preferenser → hämta preferenser
app.add_url_rule("/preferenser", view_func=las_preferenser, methods=["GET"])
print("✅ /preferenser (GET) registrerad")


if __name__ == "__main__":
    print("🚀 Startar Flask-server...")
    app.run(host="0.0.0.0", port=8000)
