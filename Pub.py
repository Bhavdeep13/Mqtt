import time #Calculate time
import random #Genrate random data
import threading #Multi tasking
import paho.mqtt.client as mqtt #MQTT Protocol
from datetime import datetime, timedelta #For time calculation

#MQTT Broker Details
broker_address = "test.mosquitto.org"
broker_port = 1883

#Topics
temperature_topic = "office/environment/temperature"
humidity_topic = "office/environment/humidity"
co2_topic = "office/environment/co2"

#Smart Sensors Simulation
#Create smartsensor and genrate random sensor data
class SmartSensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id
        self.running = True

    def get_temperature(self):
        return round(random.uniform(20, 25), 2)

    def get_humidity(self):
        return round(random.uniform(40, 60), 2)

    def get_co2_concentration(self):
        return round(random.uniform(300, 700), 2)

    def simulate_sensor_data(self):
        #Start time
        #Sample Time stamp: 12:00:00
        start_time = datetime.strptime("12:00:00", "%H:%M:%S")
        current_time = start_time
        while self.running:
            #Stop after 2 hours
            if current_time.strftime("%H:%M:%S") == "14:00:00":  # Stop at 14:00:00
                break

            #print(f"{current_time.strftime('%H:%M:%S')} - {self.sensor_id} - Temperature: {self.get_temperature()}°C, Humidity: {self.get_humidity()}%, CO2: {self.get_co2_concentration()}ppm")
            #Collect data at each timeframe
            temperature_data = {
                "sensor_id": self.sensor_id,
                "value": self.get_temperature(),
                "timestamp": current_time.strftime("%H:%M:%S")
            }
            humidity_data = {
                "sensor_id": self.sensor_id,
                "value": self.get_humidity(),
                "timestamp": current_time.strftime("%H:%M:%S")
            }
            co2_data = {
                "sensor_id": self.sensor_id,
                "value": self.get_co2_concentration(),
                "timestamp": current_time.strftime("%H:%M:%S")
            }

            #Publish data to broker
            publish_message(temperature_topic, str(temperature_data))
            publish_message(humidity_topic, str(humidity_data))
            publish_message(co2_topic, str(co2_data))

            current_time += timedelta(minutes=1)  #Increment time by 1 minute
            time.sleep(0.1)  #Speed up the simulation

#Publisher Setup
publisher_client = mqtt.Client()

def publish_message(topic, message):
    publisher_client.connect(broker_address, broker_port, 60)
    publisher_client.publish(topic, message)
    publisher_client.disconnect()

#Smart Sensor Simulation
sensor1 = SmartSensor(sensor_id="sensor1")
sensor_thread = threading.Thread(target=sensor1.simulate_sensor_data)
sensor_thread.daemon = True
sensor_thread.start()

# Wait for simulation to complete
sensor_thread.join()