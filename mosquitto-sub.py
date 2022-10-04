import paho.mqtt.client as mqtt
from datetime import datetime
import sys

MQTT_SERVER="10.0.0.3" # Address of the Broker
MQTT_PATH="emergency_service" 


def on_connect(client, userdata, flags, rc):	
	client.subscribe(MQTT_PATH)
	
def on_message(client, userdata, msg):
	current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
	
	# We create a file linked to the subscriber number
	
	file_name='logs_'+sys.argv[1]+'.txt'
	
	with open(file_name, 'a') as f:
		sending_time = datetime.strptime(msg.payload.decode("utf-8"), '%Y-%m-%d %H:%M:%S.%f')
		receiving_time = datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S.%f')
		difference = receiving_time - sending_time
		st=str(difference)
		#In this file we save the elapsed time between the emission and reception of the message
		
		f.write(st[8:-3] + '\n')
	
client=mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_SERVER, 1883, 60)

client.loop_forever()
