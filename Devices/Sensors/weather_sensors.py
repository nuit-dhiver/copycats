import random
import pyowm
from datetime import datetime

class weather_sensors:


    def __init__(self, api_key, location, unit='celsius'):

        self.sensor_serial = random.randrange(10000,99999)
        self.location = location
        self.api_key = api_key
        self.open_wmap = pyowm.OWM(self.api_key)
        self.manager = self.open_wmap.weather_manager()
        self.weather_location = self.manager.weather_at_place(location+',CZ')
        self.data = self.weather_location.weather
        #self.sensor_type = sensor_type
        self.unit = unit



class temperature_sensor(weather_sensors):
    
    
    def calculate_temperature(self):

            return self.data.get_temperature(unit=self.unit)

    def send(self):

        time = f'{datetime.now().year}/{datetime.now().month}/{datetime.now().day} {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}'
        return [self.sensor_type ,self.sensor_serial, self.location, time, self.calculate_temperature()]

class humidity_sensor(weather_sensors):

    def calculate_humidity(self):

        return self.data.get_humidity()


    def send(self):

        time = f'{datetime.now().year}/{datetime.now().month}/{datetime.now().day} {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}'
        return [self.sensor_type ,self.sensor_serial, self.location, time, self.calculate_humidity()]

class wind_sensor(weather_sensors):

    def calculate_wind(self):

        self.wind = self.data.get_wind()
        return [self.wind['speed'], self.wind['deg']]

    def send(self):

         time = f'{datetime.now().year}/{datetime.now().month}/{datetime.now().day} {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}'
         return [self.sensor_type ,self.sensor_serial, self.location, time, self.calculate_wind()]

