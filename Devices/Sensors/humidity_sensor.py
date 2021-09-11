import random
import json
from datetime import datetime

class humidity_sensor:

    sensor_type = 'HumiditySensor'
    sensor_type_code = 11

    def __init__(self, region, application='outdoor',location='DefaultLocation'):

        self.sensor_serial = random.randrange(10000,99999)
        self.region = region
        self.location = location
        self.application = application

    def set_coefficents(self):

        if self.region == 'dry':
            self.humidity_coefficent = 0.25
        elif self.region == 'normal':
            self.humidity_coefficent = 0.5
        elif self.region == 'humid':
            self.humidity_coefficent = 0.85

        if self.application == 'indoor':
            if self.region == 'dry':
                self.application_coefficent = 1.1
            elif self.region == 'normal':
                self.application_coefficent = 0.95
            elif self.region == 'humid':
                self.application_coefficent = 0.9
        elif self.application == 'greenhouse':
            self.application_coefficent = 0.55
            self.humidity_coefficent = 1
        elif self.application == 'outdoor':
            self.application_coefficent = 1



    def calculate(self):

        self.set_coefficents()
        relative_humidity = 100 * random.uniform(self.humidity_coefficent - 0.16, self.humidity_coefficent + 0.1) * self.application_coefficent
        if relative_humidity >= 100:
            return 100
        else:
            return round(relative_humidity)


    def send(self):

        time = f'{datetime.now().year}/{datetime.now().month}/{datetime.now().day} {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}'
        values = {
            "sensor_type" : self.sensor_type,
            "serial" : self.sensor_serial,
            "location" : self.location,
            "time" : time,
            "value" : self.calculate()
        }
        return json.dumps(values)



humid = humidity_sensor(region = 'humid', application='greenhouse')
print(humid.send())
