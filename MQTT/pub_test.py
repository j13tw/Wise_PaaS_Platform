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

SERVER_MQTT_SERVER = "iot.cht.com.tw"
SERVER_MQTT_TOPIC_HEAD = "/v1/device/"
SERVER_MQTT_TOPIC_END = "/rawdata"
SERVER_MQTT_PORT = 1883
SERVER_USER_NAME = ""
SERVER_USER_PWD = ""

SERVER_MQTT_TOPIC_DL303 = "DL303"
SERVER_DEVICE_ID_DL303 = "7839288845"
SERVER_DEVICE_KEY_DL303 = "DK1CSFECPSXST91BKE"

SERVER_MQTT_TOPIC_ET7044 = "ET7044"
SERVER_DEVICE_ID_ET7044 = "7839306572"
SERVER_DEVICE_KEY_ET7044 = "DKST1SRZ3CRBSZUKBF"

SERVER_MQTT_TOPIC_POWER_METER = "PowerMeter"
SERVER_DEVICE_ID_POWER_METER = "7839467604"
SERVER_DEVICE_KEY_POWER_METER = "DK4PA7GA7X55R7PKCB"

SERVER_MQTT_TOPIC_UPS_A = "UPS_A"
SERVER_DEVICE_ID_UPS_A = "7839547792"
SERVER_DEVICE_KEY_UPS_A = "DKF2SHXUGUU7942KZ3"

SERVER_MQTT_TOPIC_UPS_B = "UPS_B"
SERVER_DEVICE_ID_UPS_B = "7839666288"
SERVER_DEVICE_KEY_UPS_B = "DKTGWYSE0GCMG2ZFYC"


while(1):
    print(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
    SERVER_TOPIC = SERVER_MQTT_TOPIC_HEAD + SERVER_DEVICE_ID_UPS_A + SERVER_MQTT_TOPIC_END
    SERVER_USER_NAME = SERVER_DEVICE_KEY_UPS_A
    SERVER_USER_PWD = SERVER_DEVICE_KEY_UPS_A
    print("NAME", SERVER_USER_NAME)
    print("PWD", SERVER_USER_PWD)
    print(SERVER_TOPIC)
    mqtt_pub = mqtt.Client("CHT-IOT")
    mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
    mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
#    mqtt_pub.connect("10.20.0.19", SERVER_MQTT_PORT)
    SERVER_PUB_COMMAND = '[{"id":"batteryRemain_Percent_A", "value":["10"], "time":"2018-10-04T06:55:39.933Z"},\
    {"id":"batteryTemp_A", "value":["55"], "time":"2018-10-04T06:55:39.933Z"}, \
    {"id":"batteryVolt_A", "value":["220"], "time":"2018-10-04T06:55:39.933Z"},\
    {"id":"inputFreq_A", "value":["61.1"], "time":"2018-10-04T06:55:39.933Z"},\
    {"id":"inputLine_A", "value":["1"], "time":"2018-10-04T06:55:39.933Z"},\
    {"id":"inputVolt_A", "value":["216.0"], "time":"2018-10-04T06:55:39.933Z"},\
    {"id":"outputAmp_A", "value":["13.5454"], "time":"2018-10-04T06:55:39.933Z"},\
    {"id":"outputFreq_A", "value":["61.0"], "time":"2018-10-04T06:55:39.933Z"},\
    {"id":"outputLine_A", "value":["1"], "time":"2018-10-04T06:55:39.933Z"},\
    {"id":"outputPercent_A", "value":["39"], "time":"2018-10-04T06:55:39.933Z"},\
    {"id":"outputVolt_A", "value":["212.0"], "time":"2018-10-04T06:55:39.933Z"},\
    {"id":"outputWatt_A", "value":["3.889"], "time":"2018-10-04T06:55:39.933Z"}]'
    print(SERVER_PUB_COMMAND)
    mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
    time.sleep(3)

    now = int(datetime.datetime.now().microsecond/100)
    print(now)