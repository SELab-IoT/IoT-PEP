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
    session_manager.putInSession("scanList", scanList)
    result = json.dumps(list(scanList.keys()))
    return result


## 6. Connect request for selected Device list
## ~ 12. Return Ack message
@app.route("/devices", methods=['POST'])
def requestForConnectToDevices():
    
    def parseRequest():
        content = request.get_json()
        jsonConnectList = content.get("deviceList")
        print(type(jsonConnectList))
        connectList = json.dumps(jsonConnectList)
        return connectList
    
    connectList = parseRequest()
    scanList = session_manager.get("scanList")
    
    deviceProfiles = device_manager.connectToDevices(connectList, scanList)
    result = device_manager.updateDevices(deviceProfiles)
    return json.dumps(result)