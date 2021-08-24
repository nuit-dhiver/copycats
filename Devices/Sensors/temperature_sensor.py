import random
import pyowm
from datetime import datetime

class temperature_sensor:

    sensor_type = 'TemperatureSensor'
    sensor_type_code = 11


    def __init__(self, api_key , location, unit='celsius'):

        self.sensor_serial = random.randrange(10000,99999)
        self.location = location
        self.api_key = api_key
        self.open_wmap = pyowm.OWM(self.api_key)
        self.manager = self.open_wmap.weather_manager()
        self.weather_location = self.manager.weather_at_place(location)
        self.data = self.weather_location.get_weather()
        self.unit = unit

        

    def calculate(self):

            return self.data.get_temperature(unit=self.unit)


    def send(self):

        time = f'{datetime.now().year}/{datetime.now().month}/{datetime.now().day} {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}'
        return [self.sensor_type ,self.sensor_serial, self.location, time, self.calculate()]



        


     


