import json
from flask import Flask, request,jsonify
import time
from Sensors.light_sensor import light_sensor
from Sensors.humidity_sensor import humidity_sensor


app = Flask(__name__)
@app.route('/light')

def get_light():

    light = light_sensor()

    record = light.send()
    return jsonify(record)

@app.route('/humidity/reg=<region>_app=<application>')

def get_humidity(region='normal',application='outdoor'):

    humidity = humidity_sensor(region=region, application=application)

    record = humidity.send()
    return jsonify(record)

app.run()
