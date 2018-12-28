#-*- coding: utf-8 -*-

from application import app
from service import device_manager
from util import session_manager
from flask import request
import json
import yaml

## 2. Device Search Request
## ~ 4. Return Connectable Device List
@app.route("/devices/scan", methods=['GET'])
def appRequestDeviceList():
    scanList = device_manager.scanDeviceList()
    print("scanList : ")
    print(device_manager.scanList)
    result = json.dumps(list(scanList.keys()))
    return result


## 6. Connect request for selected Device list
## ~ 12. Return Ack message
@app.route("/devices", methods=['POST'])
def requestForConnectToDevices():
    
    def parseRequest():
        ##########################
        content = yaml.safe_load(request.get_data())
        connectList = content.get("deviceList")
##        connectList = map(lambda x:x.encode('ascii'), connectList)
        print("Debug in device_registration.py:30")
        print(content)
        print(connectList)
        print(type(connectList))
        userId = content.get("userId")
        sessionKey = content.get("sessionKey")
        loggedIn = session_manager.checkLogin(userId, sessionKey)
        
        return (connectList, loggedIn)
    
    connectList, loggedIn = parseRequest()
    
    if(loggedIn):
        scanList = device_manager.scanList
        deviceProfiles = device_manager.connectToDevices(connectList, scanList)
        print("Debug in device_registration.py : 46")
        print(deviceProfiles)
        result = device_manager.updateDevices(deviceProfiles)
    
    else:
        result = "{}"
    
    print("result : "+ json.dumps(result))
    
    return json.dumps(result)