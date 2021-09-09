import json
from flask import Flask, request,jsonify
import time
from Sensors.light_sensor import light_sensor

light = light_sensor()

app = Flask(__name__)
@app.route('/light')

def index():
    record = sensor.send()
    return jsonify(record)

app.run()
