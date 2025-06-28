from flask import Flask, jsonify
import requests

app = Flask(__name__)
climas = []

barrios = {
    "barrio1": {"name": "Cuajimalpa"},
    "barrio2": {"name": "Alvaro Obregón"},
    "barrio3": {"name": "Miguel Hidalgo"},
    "barrio4": {"name": "Coyoacán"},
    "barrio5": {"name": "Xochimilco"},
}

