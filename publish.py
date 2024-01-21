import mqtt.client as mqtt 
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io" #online broker from eclipse
client= mqtt.Client("test1")  #name client
client.connect(mqttBroker) #connect the client to the online broker

while True:
    randNumber= uniform(20.0,21.0)  #random number from 20 to 21
    client.publish("test", randNumber) #publish the random number
    print("published" + str(randNumber) + "to topic test with SUCCESSSS")  #on screen confirmation
    time.sleep(1)
