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
SERVER_MQTT_TOPIC_HEAD = "/v1/device/"
SERVER_MQTT_TOPIC_END = "/rawdata"
SERVER_MQTT_PORT = 1883
SERVER_USER_NAME = "e0f25769-8431-476a-a1dd-1176c1b6db94:c82f37e5-640d-4bc7-a923-7db90be3abf9"
SERVER_USER_PWD = "zoiXypQQKxuzz5rlvAel6q59b"

SERVER_MQTT_TOPIC_DL303 = "d9e527d26c1ea764fb87bdd236537ebm"

SERVER_MQTT_TOPIC_ET7044 = "38b1970c53e946cde9ca12efed6dc3bp"

SERVER_MQTT_TOPIC_POWER_METER = "13bed6eeecf7c893a0f5acc9241c14o5"

SERVER_MQTT_TOPIC_UPS_A = "dffafb9802d50581783ce99bcad7bez0"

SERVER_MQTT_TOPIC_UPS_B = "4497a4ad26784de5f53fc8a31d201azo"

SERVER_MQTT_TOPIC_AIR_CONDITION = "39dddf22d9507e03c86d4ac0d79ce4u9"

SERVER_MQTT_TOPIC_UPS_ROUTE_A = "bed258e5ff169da3d037dd1de66400kx"

SERVER_MQTT_TOPIC_UPS_ROUTE_B = "a9a39645df7349fddc8959bea193462b"


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
    print('------------------------------------------------------')
    print("message received -->" ,message.payload.decode('utf-8'))
    print("message topic =",message.topic)
    
    if (message.topic == CLIENT_MQTT_TOPIC_UPS_ROUTE_B):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_UPS_ROUTE_B
        print(SERVER_TOPIC)
        data = json.loads(message.payload)
        IN_V110_A = str(data['IN_V110_A']) + "A"
        IN_V110_B = str(data['IN_V110_B']) + "A"
        OUT_V110_A = str(data['OUT_V110_A']) + "A"
        OUT_V110_B = str(data['OUT_V110_B']) + "A"
        OUT_V110_C = str(data['OUT_V110_C']) + "A"
        OUT_V110_D = str(data['OUT_V110_D']) + "A"
        OUT_V110_E = str(data['OUT_V110_E']) + "A"
        mqtt_pub = mqtt.Client("CHT-IOT")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        SERVER_PUB_COMMAND = '[{"id":"IN_V110_A", "value":["' + IN_V110_A + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"IN_V110_B", "value":["' + IN_V110_B + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"OUT_V110_A", "value":["' + OUT_V110_A + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"OUT_V110_B", "value":["' + OUT_V110_B + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"OUT_V110_C", "value":["' + OUT_V110_C + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"OUT_V110_D", "value":["' + OUT_V110_D + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"OUT_V110_E", "value":["' + OUT_V110_E + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        print("------------------------------------------------")
    
    if (message.topic == CLIENT_MQTT_TOPIC_UPS_ROUTE_A):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_UPS_ROUTE_A
        print(SERVER_TOPIC)
        data = json.loads(message.payload)
        IN_V110_A = str(data['IN_V110_A']) + "A"
        IN_V110_B = str(data['IN_V110_B']) + "A"
        OUT_V110_A = str(data['OUT_V110_A']) + "A"
        OUT_V110_B = str(data['OUT_V110_B']) + "A"
        OUT_V110_C = str(data['OUT_V110_C']) + "A"
        OUT_V110_D = str(data['OUT_V110_D']) + "A"
        OUT_V110_E = str(data['OUT_V110_E']) + "A"
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        SERVER_PUB_COMMAND = '{"id":"IN_V110_A", "value":["' + IN_V110_A + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '{"id":"IN_V110_B", "value":["' + IN_V110_B + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '{"id":"OUT_V110_A", "value":["' + OUT_V110_A + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '{"id":"OUT_V110_B", "value":["' + OUT_V110_B + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '{"id":"OUT_V110_C", "value":["' + OUT_V110_C + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '{"id":"OUT_V110_D", "value":["' + OUT_V110_D + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '{"id":"OUT_V110_E", "value":["' + OUT_V110_E + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        print("------------------------------------------------")
    
    if (message.topic == CLIENT_MQTT_TOPIC_AIR_CONDITION):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_AIR_CONDITION
        print(SERVER_TOPIC)
        data = json.loads(message.payload)
        temp = str(data['Temperature']) + "℃"
        humi = str(data['Humidity']) + "%"
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        SERVER_PUB_COMMAND = '[{"id":"Humi", "value":["' + humi + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
#        print(SERVER_PUB_COMMAND)
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"Temp", "value":["' + temp + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "."+ micro_second + 'Z"}]'
#        print(SERVER_PUB_COMMAND)
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
#       print(SERVER_PUB_COMMAND)
        print("------------------------------------------------")

    if (message.topic == CLIENT_MQTT_TOPIC_POWER_METER):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_POWER_METER
        print(SERVER_TOPIC)
        data = json.loads(message.payload)
        temp = str(data['Temperature'])
        humi = str(data['Humidity'])
        current = str(data['currents'])
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        SERVER_PUB_COMMAND = '[{"id":"Current", "value":["' + current + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "."+ micro_second + 'Z"}, \
        {"id":"Humi", "value":["' + humi + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"},\
         {"id":"Temp", "value":["' + temp + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "."+ micro_second + 'Z"}]'
#       print(SERVER_PUB_COMMAND)
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        print("------------------------------------------------")
        
    if (message.topic == CLIENT_MQTT_TOPIC_UPS_MONITOR):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_UPS_A
        print(SERVER_TOPIC)
        data = json.loads(message.payload)
        inputStatus = data['input_A']
        inputLine = inputStatus['inputLine_A'] + "線路" 
        inputFreq = inputStatus['inputFreq_A'] + "HZ"
        inputVolt = inputStatus['inputVolt_A'] + "V"
        outputStatus = data['output_A']
        outputLine = outputStatus['outputLine_A'] + "線路"
        outputFreq = outputStatus['outputFreq_A'] + "HZ"
        outputVolt = outputStatus['outputVolt_A']+ "V"
        outputAmp = outputStatus['outputAmp_A']+ "A"
        outputWatt = outputStatus['outputWatt_A']
        outputPercent = outputStatus['outputPercent_A'] + "%"
        battery_status = data['battery_A']['status']
        batteryTemp = battery_status['batteryTemp_A']
        batteryVolt = battery_status['batteryVolt_A'] + "V"
        batteryRemain_Percent = battery_status['batteryRemain_Percent_A'] + "%"

        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        SERVER_PUB_COMMAND = '[{"id":"batteryRemain_Percent_A", "value":["' + batteryRemain_Percent + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"batteryTemp_A", "value":["' + batteryTemp + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"batteryVolt_A", "value":["' + batteryVolt + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"inputFreq_A", "value":["' + inputFreq + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"inputLine_A", "value":["' + inputLine + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"inputVolt_A", "value":["' + inputVolt + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"outputAmp_A", "value":["' + outputAmp + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"outputFreq_A", "value":["' + outputFreq + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"outputLine_A", "value":["' + outputLine + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"outputPercent_A", "value":["' + outputPercent + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second+ "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"outputVolt_A", "value":["' + outputVolt + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"outputWatt_A", "value":["' + outputWatt + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        print("------------------------------------------------")

        SERVER_TOPIC = SERVER_DEVICE_ID_UPS_B
        print(SERVER_TOPIC)
        inputStatus = data['input_B']
        inputLine = inputStatus['inputLine_B'] + "線路"
        inputFreq = inputStatus['inputFreq_B'] + "HZ"
        inputVolt = inputStatus['inputVolt_B'] + "V"
        outputStatus = data['output_B']
        outputLine = outputStatus['outputLine_B'] + "線路"
        outputFreq = outputStatus['outputFreq_B'] + "HZ"
        outputVolt = outputStatus['outputVolt_B'] + "V"
        outputAmp = outputStatus['outputAmp_B'] + "A"
        outputWatt = outputStatus['outputWatt_B']
        outputPersent = outputStatus['outputPercent_B'] + "%"
        battery_status = data['battery_B']['status']
        batteryTemp = battery_status['batteryTemp_B']
        batteryVolt = battery_status['batteryVolt_B'] + "V"
        batteryRemain_Percent = battery_status['batteryRemain_Percent_B'] + "%"

        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        SERVER_PUB_COMMAND = '[{"id":"batteryRemain_Percent_B", "value":["' + batteryRemain_Percent + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"batteryTemp_B", "value":["' + batteryTemp + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"batteryVolt_B", "value":["' + batteryVolt + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"inputFreq_B", "value":["' + inputFreq + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"inputLine_B", "value":["' + inputLine + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"inputVolt_B", "value":["' + inputVolt + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"outputAmp_B", "value":["' + outputAmp + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"outputFreq_B", "value":["' + outputFreq + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"outputLine_B", "value":["' + outputLine + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"outputPercent_B", "value":["' + outputPercent + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second+ "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"outputVolt_B", "value":["' + outputVolt + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        time.sleep(0.1)
        SERVER_PUB_COMMAND = '[{"id":"outputWatt_B", "value":["' + outputWatt + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        print("------------------------------------------------")
    
    if (message.topic == CLIENT_MQTT_TOPIC_DL303_CO2):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_DL303
        print(SERVER_TOPIC)
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        SERVER_PUB_COMMAND = '{"id":"co2", "value":["' + str(message.payload.decode('utf-8')) + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}'
        print(SERVER_PUB_COMMAND)
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        print("------------------------------------------------")
    
    if (message.topic == CLIENT_MQTT_TOPIC_DL303_DC):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_DL303
        print(SERVER_TOPIC)
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        SERVER_PUB_COMMAND = '[{"id":"dewp", "value":["' + str(message.payload.decode('utf-8'))  + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
#       print(SERVER_PUB_COMMAND)
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        print("------------------------------------------------")

    if (message.topic == CLIENT_MQTT_TOPIC_DL303_RH):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_DL303
        print(SERVER_TOPIC)
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        SERVER_PUB_COMMAND = '[{"id":"humi", "value":["' + str(message.payload.decode('utf-8'))  + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
#       print(SERVER_PUB_COMMAND)
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        print("------------------------------------------------")

    if (message.topic == CLIENT_MQTT_TOPIC_DL303_TC):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_DL303
        print(SERVER_TOPIC)
        mqtt_pub = mqtt.Client("Wise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        SERVER_PUB_COMMAND = '[{"id":"temp", "value":["' + str(message.payload.decode('utf-8'))  + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
#       print(SERVER_PUB_COMMAND)
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        print("------------------------------------------------")

    if (message.topic == CLIENT_MQTT_TOPIC_ET7044):
        SERVER_TOPIC = SERVER_MQTT_TOPIC_ET7044
        print(SERVER_TOPIC)
        mqtt_pub = mqtt.Client("CWise-PaaS")
        mqtt_pub.username_pw_set(SERVER_USER_NAME, password=SERVER_USER_PWD)
        mqtt_pub.connect(SERVER_MQTT_SERVER, SERVER_MQTT_PORT)
        sw = ["0", "0", "0", "0", "0", "0", "0", "0"]
        message = message.payload.decode('utf8').split("[")[1].split("]")[0]
        for x in range(0, 8):
            status = message.split(",")[x]
#            print(status)
            if (status == "false"): sw[x] = "0"
            else: sw[x] = "1"
#            print(sw[x])7
        sw[1] = "1"
        sw[4] = "1"
        sw[7] = "1"
        SERVER_PUB_COMMAND = '[{"id":"sw1", "value":[' + sw[0] + '], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"},\
                            {"id":"sw2", "value":["' + sw[1] + '"], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}, \
                            {"id":"sw3", "value":[' + sw[2] + '], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}, \
                            {"id":"sw4", "value":[' + sw[3] + '], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}, \
                            {"id":"sw5", "value":[' + sw[4] + '], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}, \
                            {"id":"sw6", "value":[' + sw[5] + '], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}, \
                            {"id":"sw7", "value":[' + sw[6] + '], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}, \
                            {"id":"sw8", "value":[' + sw[7] + '], "time":"' + year + "-" + month + "-" + day + "T" + hour + ":" + minute + ":" + second + "." + micro_second + 'Z"}]'
#       print(SERVER_PUB_COMMAND)
        mqtt_pub.publish(SERVER_TOPIC, SERVER_PUB_COMMAND)
        print("------------------------------------------------")
        
    print('MQTT To Server OK ! -->' , now)
    print('------------------------------------------------------')
    time.sleep(1)

# MQTT connection
mqtt_sub = mqtt.Client("NUTC-IMAC")
mqtt_sub.on_message = on_message
mqtt_sub.connect(CLIENT_MQTT_SERVER, CLIENT_MQTT_PORT)
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
mqtt_sub.loop_forever()