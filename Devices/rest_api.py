import json
from flask import Flask, request,jsonify
import time
from Sensors.light_sensor import light_sensor

light = light_sensor()
record = json.loads(sensor.send())

app = Flask(__name__)
@app.route('/light', methodes=['GET'])

def index():
    record = json.loads(sensor.send())
    return jsonify(record)

app.run()
