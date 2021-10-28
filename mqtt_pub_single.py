import paho.mqtt.publish as publish
import json

BROKER = 'hanage'
PORT = 1883
TOPIC = "rspi/env"
# username = 'user'
# password = 'pass'

class mqtt_pub_single():
    def __init__(self, topic=TOPIC, broker=BROKER, port=PORT) -> None:
        self.topic = topic
        self.broker = broker
        self.port = port
        pass
    def pub_single(self, data):
        msg = json.dumps(data)
        publish.single(self.topic, msg, hostname=self.broker, port=self.port)

def main():
    data = {'tmp': 23.0, 'hum': 54.0, 'atm':998.0}
    msg = json.dumps(data)
    publish.single(TOPIC, msg, hostname=BROKER, port=PORT)

if __name__ == '__main__':
    main()