import paho.mqtt.publish as publish
import json

broker = 'host'
port = 1883
topic = "rspi/env"
# username = 'user'
# password = 'pass'
data = {'tmp': 23.0, 'hum': 54.0, 'atm':998.0}
msg = json.dumps(data)
publish.single(topic, msg, hostname=broker, port=port)