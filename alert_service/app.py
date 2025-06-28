from flask import Flask, request, jsonify


app = Flask(__name__)
alertas = []

@app.route("/alert", methods=["POST"])
def alert():
   data = request.json
   if data["tipo"] == "temperatura" and data["valor"] > 30:
        alerta = {
            "barrio": data["barrio"],
            "mensaje": f"Temperatura alta: {data['valor']}°C",
        }
        alertas.append(alerta)
        print(f"ALERTA: {alerta}")
        return "Alerta procesada", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)



