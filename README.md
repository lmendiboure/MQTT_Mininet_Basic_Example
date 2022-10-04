This project simply proposes a simple example of a code enabling to deploy MQTT in a Mininet environment and to automatically launch a broker (with a remote access) and clients (MQTT Subscribers).

In this considered architecture (mqtt-example.py that can be used to launch this project) h3 is considered as a broker and h1 and h2 as MQTT clients. Both broker and clients are launched when this file is launched using python.

The broker deployed within this file uses a simple config file (mosquitto.conf) to enable remote access (h1, h2 in this example). Note that this config file should usually be placed in a specific folder (/etc/mosquitto). Also note that as this file calls another file (mosquitto-sub.py) both these files (mqtt-example + mosquitto-sub) should be placed in a same folder.

In the considered example, the MQTT Publisher (currently launched once Mininet is running through a simple command line xterm h* + python mosquitto-pub.py) only sends the current time to the subscribers. The idea is to be able to compute the elasped time between the emission and reception of the message. To this end, once it receives the message, the subscriber also computes the current time and the difference between this time and the emission time. This information (in milliseconds) is then stored in a log file (such a file is created for each subscriber). 

Also note that, the generation of messages, from one ore several publishers, could simply be added to the mqtt-example.py file thanks to the cmd command (an example of usage of this command for subscribers is already showed in this file). The idea could be to periodically generate messages to compute different elapsed time between emission and reception in different network configurations.

Last note: the currently used MQTT Topic is called "emergency_service".
