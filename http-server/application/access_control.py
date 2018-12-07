from application import app
from service import device_manager, platform_manager
from util import session_manager, xacml_request_builder
import json
from flask import request

# 4. Access Control(XACML Request)
## 1. Device Access Request
## ~ 4. Return Permit or Deny
@app.route("/devices/<deviceName>", methods=['POST'])
def requestForAccessToDevice(deviceName):
    
    def parseRequest():
        content = json.loads(request.get_data())
        actionId = content.get("actionId")
        actionName = content.get("actionName")
        params = content.get("params")
        deviceId = content.get("deviceId")
        #print(actionId, actionName, params, deviceId)
        
        userId = content.get("userId")
        sessionKey = content.get("sessionKey")
        loggedIn = session_manager.checkLogin(userId, sessionKey)
        
        return (actionId, actionName, params,deviceId, loggedIn)
    
    # TODO: remove hardcode -> replace it read profile file.
    pepId = "pep_1" 
    
    actionId, actionName, params, deviceId, loggedIn = parseRequest()
    
    if(loggedIn):
    
        bundle = {"pepId":pepId, "body":{"userId":userId, "deviceName":deviceName, "actionId":actionId, "actionName":actionName, "params":params,"deviceId":deviceId}}
        payload = xacml_request_builder.buildRequest(bundle)
        result = platform_manager.queryToPDP(payload)
        
        #mock up the value of result for testing
        result["decision"]=True
        
        if(result["decision"]):
            values = list(map(lambda p: p["value"], params))
            device_manager.accessToDevice(deviceName, actionName, values)
            
    else:
        result = "{}"
    
    return json.dumps(result)