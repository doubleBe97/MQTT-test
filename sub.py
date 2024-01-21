import mqtt.client as mqtt
from random import randrange, uniform
import time

def on_message(client,userdata,message):
    print("received message: " + str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io"
client= mqtt.Client("TEST2")
client.connect(mqttBroker)

client.loop_start()
client.subscribe("test")
client.on_message = on_message
time.sleep(10)
client.loop_end()
