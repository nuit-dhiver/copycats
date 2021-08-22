from confluent_kafka import Producer
from Sensors.light_sensor import light_sensor
import time
import socket


sensor = light_sensor('LocationOfSensor')
producer = Producer({'bootstrap.servers':'192.168.64.6:9092', 'client.id': socket.gethostname()})
time_frame = 1
topic = 'greenhouse_light'


def delivery_report(error, msg):

    if error is not None:
        print('Message delivery failed {}'.format(error))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


while True:

    producer.poll(0)
    producer.produce(topic, str(sensor.send()), callback = delivery_report)
    time.sleep(time_frame)

