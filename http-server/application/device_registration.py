from application import app
from service import device_manager
from util import session_manager
import json

## 2. Device Search Request
## ~ 4. Return Connectable Device List
@app.route("/devices/scan", methods=['GET'])
def appRequestDeviceList(userId):
    scanList = device_manager.scanDeviceList(userId)
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
        connectList = json.loads(jsonConnectList)
        return connectList
    
    connectList = parseRequest()
    scanList = session_manager.get("scanList")
    
    result = device_manager.connectToDevices(connectList, scanList) # ack or nack
    return result