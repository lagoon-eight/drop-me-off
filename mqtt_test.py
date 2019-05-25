import time
import paho.mqtt.client as paho
broker="192.168.0.12"

#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print ("Topic = " + message.topic)
    print("received message =",str(message.payload.decode("utf-8")))

client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("picar/control/left")#subscribe
time.sleep(2)
print("publishing ")
client.publish("picar/control/left","5")#publish
time.sleep(4)
client.disconnect() #disconnect
client.loop_stop() #stop loop