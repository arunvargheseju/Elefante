#Program to send data to IOT CONNECT dashboard 
import sys
import json
import time
import threading
import gps
import ei
from iotconnect import IoTConnectSDK
from datetime import datetime

env = "Avnet"
uniqueId = "Device ID"
cpId = "Your Company ID"
interval = 60

tProcess = None
dataArray = []
gps = gps.gps()

def callbackMessage(msg):
    if msg:
        print("\n--- Command Message Received ---")
        print(str(msg['ack']))
        print(str(msg['ackId']))
        print(str(msg['command']))
        print(str(msg['uniqueId']))

def callbackTwinMessage(msg):
    if msg:
        print("\n--- Twin Message Received ---")
        print(json.dumps(msg))

def sendBackToSDK(sdk, dataArray):
    global tProcess
    sdk.SendData(dataArray)
    time.sleep(interval)
    tProcess = None

def processData(data):
        value = data
        return value   


def sendtoiot(argv):
    global tProcess, dataArray
    try:
        with IoTConnectSDK(cpId, uniqueId, callbackMessage, callbackTwinMessage, env) as sdk:
            try:
                dataArray = []
                data = processData(gps)
                if data != None:
                    dObj = {
                            "uniqueId": uniqueId,
                            "time": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.000Z"),
                            "data": data
                        }
                    dataArray.append(dObj)
                    
                if tProcess == None and len(dataArray) == 1:
                    tProcess = threading.Thread(target = sendBackToSDK, args = [sdk, dataArray])
                    tProcess.setName("SEND")
                    tProcess.daemon = True
                    tProcess.start()
                    tProcess.join(1)
            except KeyboardInterrupt:
                sys.exit(0)
    except Exception as ex:
        print(ex)
        sys.exit(0)

if __name__ == "__main__":
    sendtoiot(sys.argv)
