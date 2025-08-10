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


# POST /loggrorelse → separat rörelse-endpoint (om ni vill)
app.add_url_rule("/loggrorelse", view_func=logg_rorelse, methods=["POST"])
print("✅ /loggrorelse registrerad")


# POST /preferenser → hämta preferenser via JSON-body
app.add_url_rule("/preferenser", view_func=las_preferenser, methods=["POST"])
print("✅ /preferenser (POST) registrerad")



if __name__ == "__main__":
    print("🚀 Startar Flask-server...")
    app.run(host="0.0.0.0", port=8000)
