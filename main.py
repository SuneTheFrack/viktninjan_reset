from flask import Flask
from logg_router import logg_allt
from viktlogg import logg_vikt
from rorelselogg import logg_rorelse

app = Flask(__name__)

@app.route('/')
def home():
    return "ViktNinjan är igång!", 200

# Knyt alla logg-endpoints
app.add_url_rule("/logg", view_func=logg_allt, methods=["POST"])
app.add_url_rule("/loggvikt", view_func=logg_vikt, methods=["POST"])
app.add_url_rule("/loggrorelse", view_func=logg_rorelse, methods=["POST"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
