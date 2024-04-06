import paho.mqtt.client as mqtt
from datetime import datetime

# MQTT Broker Details
broker_address = "test.mosquitto.org"
broker_port = 1883

# Topics
temperature_topic = "office/environment/temperature"
humidity_topic = "office/environment/humidity"
co2_topic = "office/environment/co2"

# MQTT Subscriber Setup
#On_connect is used to make sure connection is set up properly
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe([(temperature_topic, 0), (humidity_topic, 0), (co2_topic, 0)])

#On_message is used to receive messages from the broker
def on_message(client, userdata, msg):
    current_time = datetime.now().strftime('%H:%M:%S')
    print(f"Received message: {msg.topic} - {msg.payload.decode()}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, broker_port, 60)
client.loop_forever()
