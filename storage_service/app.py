from flask import request, Flask, jsonify
import requests
import random
app = Flask(__name__)
climas = []

barrios = {
    "barrio1": {"name": "Cuajimalpa"},
    "barrio2": {"name": "Alvaro Obregón"},
    "barrio3": {"name": "Miguel Hidalgo"},
    "barrio4": {"name": "Coyoacán"},
    "barrio5": {"name": "Xochimilco"},
}

@app.route("/clima", methods=["POST"])
def clima():
    data = request.json
    barrio = random.choice(barrios)
    if barrio in barrios:
        clima_data = {
            "barrio": barrio,
            "temperatura": data["temperatura"],
            "humedad": data["humedad"],
        }
        climas.append(clima_data)
@app.route("/climas", methods=["GET"])
def get_climas():
    return jsonify(climas), 200
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)