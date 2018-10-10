#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

import serial, time
import json
import datetime
import paho.mqtt.client as mqtt

# MQTT setup data
CLIENT_MQTT_SERVER = "10.20.0.19"
CLIENT_MQTT_PORT = 1883

CLIENT_MQTT_TOPIC_DL303_CO2 = "DL303/CO2"
CLIENT_MQTT_TOPIC_DL303_RH = "DL303/RH"
CLIENT_MQTT_TOPIC_DL303_TC = "DL303/TC"
CLIENT_MQTT_TOPIC_DL303_DC = "DL303/DC"

CLIENT_MQTT_TOPIC_ET7044 = "ET7044/DOstatus"

CLIENT_MQTT_TOPIC_POWER_METER = "current"

CLIENT_MQTT_TOPIC_UPS_MONITOR = "UPS_Monitor"

CLIENT_MQTT_TOPIC_AIR_CONDITION = "air-conditioner-vent"

CLIENT_MQTT_TOPIC_UPS_ROUTE_A = "cabinet_A"
CLIENT_MQTT_TOPIC_UPS_ROUTE_B = "cabinet_B"

SERVER_MQTT_SERVER = "iothub-single-949df24b-9261-4be0-8978-d47e432bf25d-001.eastasia.cloudapp.azure.com"
SERVER_MQTT_PORT = 1883
SERVER_USER_NAME = "e0f25769-8431-476a-a1dd-1176c1b6db94:c82f37e5-640d-4bc7-a923-7db90be3abf9"
SERVER_USER_PWD = "zoiXypQQKxuzz5rlvAel6q59b"

SEVER_MQTT_TOPIC_DASHBOARD_TOPIC = "e0f25769-8431-476a-a1dd-1176c1b6db94"
SEVER_DEVICE_ID_DASHBOARD = "e0f25769-8431-476a-a1dd-1176c1b6db94:fdc0c406-d458-4594-96d1-27af027c68ee"
SEVER_DEVICE_ID_DASHBOARD = "ExqEGZuafTwERYUeeccLIPTjR"

SERVER_MQTT_TOPIC_DL303 = "d9e527d26c1ea764fb87bdd236537ebm"

SERVER_MQTT_TOPIC_ET7044 = "38b1970c53e946cde9ca12efed6dc3bp"

SERVER_MQTT_TOPIC_POWER_METER = "13bed6eeecf7c893a0f5acc9241c14o5"

SERVER_MQTT_TOPIC_UPS = "dffafb9802d50581783ce99bcad7bez0"

SERVER_MQTT_TOPIC_AIR_CONDITION = "39dddf22d9507e03c86d4ac0d79ce4u9"

SERVER_MQTT_TOPIC_UPS_ROUTE_A = "bed258e5ff169da3d037dd1de66400kx"

SERVER_MQTT_TOPIC_UPS_ROUTE_B = "a9a39645df7349fddc8959bea193462b"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    mqtt_sub.subscribe(CLIENT_MQTT_TOPIC_DL303_CO2)
    mqtt_sub.subscribe(CLIENT_MQTT_TOPIC_DL303_DC)
    mqtt_sub.subscribe(CLIENT_MQTT_TOPIC_DL303_RH)
    mqtt_sub.subscribe(CLIENT_MQTT_TOPIC_DL303_TC)
    mqtt_sub.subscribe(CLIENT_MQTT_TOPIC_ET7044)
    mqtt_sub.subscribe(CLIENT_MQTT_TOPIC_POWER_METER)
    mqtt_sub.subscribe(CLIENT_MQTT_TOPIC_UPS_MONITOR)
    mqtt_sub.subscribe(CLIENT_MQTT_TOPIC_AIR_CONDITION)
    mqtt_sub.subscribe(CLIENT_MQTT_TOPIC_UPS_ROUTE_A)
    mqtt_sub.subscribe(CLIENT_MQTT_TOPIC_UPS_ROUTE_B)

def on_message(client, userdata, message):
    now = datetime.datetime.now()
    year = str(now.year)
    month = str(now.month)
    if (int(month) < 10): month = "0" + str(month)
    day = str(now.day)
    if (int(day) < 10): day = "0" + str(day)
    hour = str(now.hour)
    if (int(hour) < 10): hour = "0" + str(hour)
    minute = str(now.minute)
    if (int(minute) < 10): minute = "0" + str(minute)
    second = str(now.second)
    if (int(second) < 10): second = "0" + str(second)
    micro_second = str(int(datetime.datetime.now().microsecond/100))
    time_stamp = '"' +year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"'
    print(time_stamp)
    print('------------------------------------------------------')
    print("message received -->" ,message.payload.decode('utf-8'))
    print("message topic =",message.topic)

    if (message.topic == CLIENT_MQTT_TOPIC_UPS_ROUTE_B):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_UPS_ROUTE_B
        print(SERVER_TOPIC)
        data = json.loads(message.payload.decode('utf-8'))
#        data["date"] = time_stamp
#        print(data)
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        mqtt_pub.publish(SERVER_TOPIC, str(data).replace("'", '"'))
        print("------------------------------------------------")
    
    if (message.topic == CLIENT_MQTT_TOPIC_UPS_ROUTE_A):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_UPS_ROUTE_A
        print(SERVER_TOPIC)
        data = json.loads(message.payload.decode('utf-8'))
#        data["date"] = time_stamp
#        print(data)
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        mqtt_pub.publish(SERVER_TOPIC, str(data).replace("'", '"'))
        print("------------------------------------------------")
    
    if (message.topic == CLIENT_MQTT_TOPIC_AIR_CONDITION):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_AIR_CONDITION
        print(SERVER_TOPIC)
        data = json.loads(message.payload.decode('utf-8'))
#        data["date"] = time_stamp
#        print(data)
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        mqtt_pub.publish(SERVER_TOPIC, str(data).replace("'", '"'))
        print("------------------------------------------------")

    if (message.topic == CLIENT_MQTT_TOPIC_POWER_METER):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_POWER_METER
        print(SERVER_TOPIC)
        data = json.loads(message.payload.decode('utf-8'))
#        data["date"] = time_stamp
#        print(data)
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        mqtt_pub.publish(SERVER_TOPIC, str(data).replace("'", '"'))
        print("------------------------------------------------")
        
    if (message.topic == CLIENT_MQTT_TOPIC_UPS_MONITOR):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_UPS
        print(SERVER_TOPIC)
        data = json.loads(message.payload.decode('utf-8'))
#        data["date"] = time_stamp
#        print(data)
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        mqtt_pub.publish(SERVER_TOPIC, str(data).replace("'", '"'))
        print("------------------------------------------------")
    
    if (message.topic == CLIENT_MQTT_TOPIC_DL303_CO2):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_DL303
        print(SERVER_TOPIC)
        data = message.payload.decode('utf-8')
#        data = {"status": data, "date": time_stamp}
#        print(data)
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        mqtt_pub.publish(SERVER_TOPIC, str(data))
        print("------------------------------------------------")
    
    if (message.topic == CLIENT_MQTT_TOPIC_DL303_DC):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_DL303
        print(SERVER_TOPIC)
        data = message.payload.decode('utf-8')
#        data = {"status": data, "date": time_stamp}
#        print(data)
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        mqtt_pub.publish(SERVER_TOPIC, data)
        print("------------------------------------------------")

    if (message.topic == CLIENT_MQTT_TOPIC_DL303_RH):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_DL303
        print(SERVER_TOPIC)
        data = message.payload.decode('utf-8')
#        data = {"status": data, "date": time_stamp}
#        print(data)
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        mqtt_pub.publish(SERVER_TOPIC, data)
        print("------------------------------------------------")

    if (message.topic == CLIENT_MQTT_TOPIC_DL303_TC):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_DL303
        print(SERVER_TOPIC)
        data = message.payload.decode('utf-8')
#        data = {"status": data, "date": time_stamp}
#        print(data)
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        mqtt_pub.publish(SERVER_TOPIC, data)
        print("------------------------------------------------")

    if (message.topic == CLIENT_MQTT_TOPIC_ET7044):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_ET7044
        print(SERVER_TOPIC)
        data = message.payload.decode('utf-8')
#        data = {"status": data, "date": time_stamp}
#        print(data)
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        mqtt_pub.publish(SERVER_TOPIC, data)
        print("------------------------------------------------")
     
    print('MQTT To Server OK ! -->' , now)
    print('------------------------------------------------------')
    time.sleep(1)

# MQTT connection
mqtt_sub = mqtt.Client("NUTC-IMAC")
mqtt_sub.on_connect = on_connect
mqtt_sub.on_message = on_message
mqtt_sub.connect(CLIENT_MQTT_SERVER, CLIENT_MQTT_PORT)
mqtt_sub.loop_forever()