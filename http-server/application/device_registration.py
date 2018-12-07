#-*- coding: utf-8 -*-

from application import app
from service import device_manager
from util import session_manager
from flask import request
import json

## 2. Device Search Request
## ~ 4. Return Connectable Device List
@app.route("/devices/scan", methods=['GET'])
def appRequestDeviceList():
    scanList = device_manager.scanDeviceList()
    result = json.dumps(list(scanList.keys()))
    return result


## 6. Connect request for selected Device list
## ~ 12. Return Ack message
@app.route("/devices", methods=['POST'])
def requestForConnectToDevices():
    
    def parseRequest():
        ##########################
        content = json.loads(request.get_data(), encoding="utf-8")
        connectList = content.get("deviceList")
        
        userId = content.get("userId")
        sessionKey = content.get("sessionKey")
        loggedIn = session_manager.checkLogin(userId, sessionKey)
        
        return (connectList, loggedIn)
    
    connectList, loggedIn = parseRequest()
    
    if(loggedIn):
        scanList = session_manager.scanList
        
        print("connectList : ")
        print(connectList)
        
        print("scanList : ")
        print(scanList)
        
        deviceProfiles = device_manager.connectToDevices(connectList, scanList)
        
        print("deviceProfiles : ")
        print(deviceProfiles)
        
        result = device_manager.updateDevices(deviceProfiles)
    
    else:
        result = "{}"
    
    print("result : "+ json.dumps(result))
    
    return json.dumps(result)