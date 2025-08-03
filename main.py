from flask import Flask
from logg_router import logg_allt
from routes.logg_get import las_loggar
from viktlogg import logg_vikt
from rorelselogg import logg_rorelse

print("✅ Flask och imports klara")  # <--- Lägg till

app = Flask(__name__)

@app.route('/')
def home():
    return "ViktNinjan är igång!", 200
    
print("✅ Flask-app initierad")  # <--- Lägg till

# Knyt alla logg-endpoints
app.add_url_rule("/logg", view_func=logg_allt, methods=["POST"])
print("✅ /logg är registrerad")

app.add_url_rule("/loggvikt", view_func=logg_vikt, methods=["POST"])
print("✅ /loggvikt registrerad")  # <--- Lägg till

app.add_url_rule("/loggrorelse", view_func=logg_rorelse, methods=["POST"])
print("✅ /loggrorelse registrerad")  # <--- Lägg till

app.add_url_rule("/logg", view_func=las_loggar, methods=["GET"])
print("✅ /logg (GET) registrerad")

if __name__ == "__main__":
    print("🚀 Startar Flask-server...")  # <--- Lägg till
    app.run(host="0.0.0.0", port=8000)
