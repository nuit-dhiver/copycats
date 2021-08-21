
import random
from datetime import date, datetime

class light_sensor:

    sensor_type = 'LightSensor'
    sensor_type_code = 10

    def __init__(self, location):

        self.sensor_serial = random.randrange(10000,99999)
        self.location = location
    
    #def setting(self, time_frame=60, send_datetime = False):

        #self.time_frame = time_frame
        #self.current_month = current_month
        #self.current_time = current_time

    def set_coefficents(self):

        self.current_hour = datetime.now().hour
        self.current_month = datetime.now().month

        if self.current_hour <= 5 or self.current_hour >= 20 :
            self.hour_coefficent = 0.1
        elif self.current_hour == 19:
            self.hour_coefficent = 0.4
        elif self.current_hour == 18:
            self.hour_coefficent = 0.5
        elif self.current_hour == 17:
            self.hour_coefficent = 0.6
        elif self.current_hour == 16:
            self.hour_coefficent = 0.7
        elif self.current_hour == 15:
            self.hour_coefficent = 0.8
        elif self.current_hour == 14:
            self.hour_coefficent = 0.9
        elif self.current_hour == 13:
            self.hour_coefficent = 1
        elif self.current_hour == 12:
            self.hour_coefficent = 0.9
        elif self.current_hour == 11:
            self.hour_coefficent = 0.8
        elif self.current_hour == 10:
            self.hour_coefficent = 0.7
        elif self.current_hour == 9:
            self.hour_coefficent = 0.6
        elif self.current_hour == 8:
            self.hour_coefficent = 0.5
        elif self.current_hour == 7:
            self.hour_coefficent = 0.4
        elif self.current_hour == 6:
            self.hour_coefficent = 0.3

        if self.current_month >= 1 and self.current_month <= 3:
            self.month_coefficent = 0.8
        elif self.current_month > 3 and self.current_month <= 6:
            self.month_coefficent = 1
        elif self.current_month >= 6 and self.current_month <= 9:
            self.month_coefficent = 0.8
        else:
            self.month_coefficent = 0.6
        

    def calculate(self):

        self.set_coefficents()
        light_intensity = 100 * random.uniform(self.hour_coefficent - 0.1, self.hour_coefficent + 0.1) * self.month_coefficent
        if light_intensity >= 100:
            return 100
        else:
            return round(light_intensity)


    def send(self):
        time = f'{datetime.now().year}/{datetime.now().month}/{datetime.now().day} {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}'
        return [self.sensor_type ,self.sensor_serial, self.location, time, self.calculate()]


        


     


