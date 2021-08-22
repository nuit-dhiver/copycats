from confluent_kafka import Producer
import light_sensor.sensors as light_sensor

sensor = light_sensor('LocationOfSensor', shading_coefficent = 1)
producer = Producer({'bootstrap.servers':'broker1, broker2'})
time_frame = 60
topic = '<SetTopicNameHere!>'


def delivery_report(error, msg):

    if error is not None:
        print('Message delivery failed {}'.format(error))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


while True:

    producer.poll(0)
    producer.produce(topic, sensor.send(), callback = delivery_report)
    sleep(time_frame)

