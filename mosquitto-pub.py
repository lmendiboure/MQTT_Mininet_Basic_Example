# In this simple publish example, we only send the current time when the message is sent: the idea is to be able to compute the elapsed time when this message is received by the receiver

import paho.mqtt.publish as publish
from datetime import datetime

MQTT_SERVER = "10.0.0.3" # need to be changed to correspond to the server @
MQTT_PATH="emergency_service" 

msg=datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
publish.single(MQTT_PATH,msg,hostname=MQTT_SERVER)
