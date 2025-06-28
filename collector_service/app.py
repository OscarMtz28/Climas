from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/data", methods=['POST'])
def add_info():
    data = request.json
    requests.post('http://storage_service:5003/storage', json=data)
    requests.post('http://alert_service:5004/alert', json=data)
    return jsonify({"Informacion enviada a storage service y alert service"}),201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

