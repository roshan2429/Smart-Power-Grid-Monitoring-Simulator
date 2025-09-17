import paho.mqtt.client as mqtt
from influxdb import InfluxDBClient
import json
import os

INFLUX_DB = os.getenv("INFLUX_DB", "powergrid")
BROKER = os.getenv("MQTT_BROKER", "localhost")
PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPIC = os.getenv("MQTT_TOPIC", "smartgrid/sensor")

influx = InfluxDBClient(os.getenv("INFLUX_HOST", "localhost"), 8086, os.getenv("INFLUX_USER", "root"), os.getenv("INFLUX_PASSWORD", "root"), INFLUX_DB)

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    # Convert non-float fields if needed
    fields = {}
    for k, v in data.items():
        if isinstance(v, (int, float)):
            fields[k] = v
        else:
            try:
                fields[k] = float(v)
            except:
                # Skip non-numeric fields in fields, store as tags if needed
                pass
    influx.write_points([{
        "measurement": "grid_metrics",
        "fields": fields
    }])
    print("Stored:", data)

client = mqtt.Client("Collector")
client.on_message = on_message
client.connect(BROKER, PORT)
client.subscribe(TOPIC)
client.loop_forever()
