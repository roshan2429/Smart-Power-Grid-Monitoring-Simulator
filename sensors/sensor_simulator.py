import paho.mqtt.client as mqtt
import json, time, random

BROKER = "localhost"
PORT = 1883
TOPIC = "smartgrid/sensor"

client = mqtt.Client("SensorPublisher")
client.connect(BROKER, PORT)

while True:
    data = {
        "voltage": round(random.uniform(210, 250), 2),
        "current": round(random.uniform(5, 20), 2),
        "frequency": round(random.uniform(49.5, 50.5), 2),
        "load": round(random.uniform(0.5, 1.5), 2),
        "status": "OK"
    }

    if random.random() < 0.05:
        data["status"] = "FAULT"

    client.publish(TOPIC, json.dumps(data))
    print(f"Published: {data}")
    time.sleep(2)
