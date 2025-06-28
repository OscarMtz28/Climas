from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
alertas = []

@app.route("/alert", methods=["POST"])
def alert():
    data = request.get_json()
    temp = data.get("temperatura")

    if temp > 10:
        jsonify({"Tmperatura excede el limite"})
    elif temp <15:
        jsonify({"Temperatura por debajo del limite"})

    return jsonify({"message": "No alert"}), 200





## SE VA A MIMIR BAI :D ## 
