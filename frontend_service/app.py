from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/consulta/<barrio>', methods=['GET'])
def consulta_barrio(barrio):

    datos_response = requests.get(f'http://storage_service:5003/query/{barrio}')
    try:
        datos = datos_response.json()
    except:
        datos = {}

    alertas_response = requests.get(f'http://alert_service:5004/alerts/{barrio}')
    try:
        alertas = alertas_response.json()
    except:
        alertas = []

    resultado = {
        "datos": datos,
        "alertas": alertas
    }

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)