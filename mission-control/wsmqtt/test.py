import paho.mqtt.publish as paho
from vars import *

paho.single("rover/command","MIS33333SIM",hostname=mqttServer)

