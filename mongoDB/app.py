import datetime
import json
import paho.mqtt.client as mqtt
from pymongo import MongoClient

# MQTT setup data
CLIENT_MQTT_SERVER = "10.20.0.19"
CLIENT_MQTT_PORT = 1883

client = MongoClient(
    'mongodb://mongodb-single-949df24b-9261-4be0-8978-d47e432bf25d-001.eastasia.cloudapp.azure.com:27017/')

db = client['e973cd66-c49a-4c4e-8d85-330ceb44b7db']
db.authenticate('b1cccb38-7abe-4511-8800-e5275780a19f',
                'QTLxUraQXnubu4qCgoviSwObQ')

DL303_CO2 = db['DL303_CO2']
DL303_RH = db['DL303_RH']
DL303_TC = db['DL303_TC']
DL303_DC = db['DL303_DC']
ET7044_DOstatus = db['ET7044_DOstatus']
current = db['current']
UPS_Monitor = db['UPS_Monitor']
air_conditioner_vent = db['air_conditioner_vent']
cabinet_A = db['cabinet_A']
cabinet_B = db['cabinet_B']


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("DL303/CO2")
    client.subscribe("DL303/RH")
    client.subscribe("DL303/TC")
    client.subscribe("DL303/DC")
    client.subscribe("ET7044/DOstatus")
    client.subscribe("current")
    client.subscribe("UPS_Monitor")
    client.subscribe("air-conditioner-vent")
    client.subscribe("cabinet_A")
    client.subscribe("cabinet_B")


def on_message(client, userdata, msg):
    topic = msg.topic
    if topic == "DL303/CO2":
        data = {"data": msg.payload.decode(
            'utf-8'), "date": datetime.datetime.utcnow()}
        print("DL303/CO2 ", data)
        _id = DL303_CO2.insert_one(data).inserted_id
        print(_id)
    if topic == "DL303/RH":
        data = {"data": msg.payload.decode(
            'utf-8'), "date": datetime.datetime.utcnow()}
        print("DL303/RH", data)
        _id = DL303_RH.insert_one(data).inserted_id
        print(_id)
    if topic == "DL303/TC":
        data = {"data": msg.payload.decode(
            'utf-8'), "date": datetime.datetime.utcnow()}
        print("DL303/TC ", data)
        _id = DL303_TC.insert_one(data).inserted_id
        print(_id)
    if topic == "DL303/DC":
        data = {"data": msg.payload.decode(
            'utf-8'), "date": datetime.datetime.utcnow()}
        print("DL303/DC ", data)
        _id = DL303_DC.insert_one(data).inserted_id
        print(_id)
    if topic == "ET7044/DOstatus":
        data = {"status": msg.payload.decode(
            'utf-8'), "date": datetime.datetime.utcnow()}
        print("ET7044/DOstatus ", data)
        _id = ET7044_DOstatus.insert_one(data).inserted_id
        print(_id)
    if topic == "current":
        data = json.loads(msg.payload.decode('utf-8'))
        data["date"] = datetime.datetime.utcnow()
        print("current ", data)
        _id = current.insert_one(data).inserted_id
        print(_id)
    if topic == "UPS_Monitor":
        data = json.loads(msg.payload.decode('utf-8'))
        data["date"] = datetime.datetime.utcnow()
        print("UPS_Monitor ", data)
        _id = UPS_Monitor.insert_one(data).inserted_id
        print(_id)
    if topic == "air-conditioner-vent":
        data = json.loads(msg.payload.decode('utf-8'))
        data["date"] = datetime.datetime.utcnow()
        print("air-conditioner-vent ", data)
        _id = air_conditioner_vent.insert_one(data).inserted_id
        print(_id)
    if topic == "cabinet_A":
        data = json.loads(msg.payload.decode('utf-8'))
        data["date"] = datetime.datetime.utcnow()
        print("cabinet_A ", data)
        _id = cabinet_A.insert_one(data).inserted_id
        print(_id)
    if topic == "cabinet_B":
        data = json.loads(msg.payload.decode('utf-8'))
        data["date"] = datetime.datetime.utcnow()
        print("cabinet_B ", data)
        _id = cabinet_B.insert_one(data).inserted_id
        print(_id)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(CLIENT_MQTT_SERVER, CLIENT_MQTT_PORT)
client.loop_forever()
