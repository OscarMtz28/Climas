from flask import Flask, request, jsonify
import random
app = Flask(__name__)
sensors = {}

@app.route("/sensors", methods=['POST'])
def add_info():
    data = request.get_json()
    sensores = str(len(sensors) + 1)
    sensors[sensores] = {
        "temperatura": data.get("temperatura", random.uniform(0, 60)),
        "humedad": data.get("humedad", random.uniform(0, 100)),
        "aire": data.get("aire", random.uniform(0, 300))
    }
    return jsonify(sensors[sensores]),201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
