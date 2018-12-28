#-*- coding: utf-8 -*-

from application import app
from service import device_manager, platform_manager
from util import session_manager, xacml_request_builder
import json
import yaml
from flask import request
from util import profile_manager

# 4. Access Control(XACML Request)
## 1. Device Access Request
## ~ 4. Return Permit or Deny
@app.route("/devices/<deviceId>", methods=['POST'])
def requestForAccessToDevice(deviceId):
    
    def parseRequest():
        content = yaml.safe_load(request.get_data())
        print("Debug in access_control.py : 18")
        print(content)
        actionId = content.get("actionId")
        actionName = content.get("actionName")
        params = content.get("params")
        deviceName = content.get("deviceName")
        macAddress = content.get("macAddress")
        userId = content.get("userId")
        sessionKey = content.get("sessionKey")
        bundle = (userId, sessionKey, actionId, actionName, params, deviceName, macAddress)
        print("Debug in access_control.py : 28")
        print(bundle)
        return bundle
    
    pepId =  profile_manager.getPEPId()
    
    userId, sessionKey, actionId, actionName, params, deviceName, macAddress = parseRequest()
    loggedIn = session_manager.checkLogin(userId, sessionKey)
    
    if(loggedIn):
    
        bundle = {"pepId":pepId, "body":{"userId":userId, "deviceName":deviceName, "actionId":actionId, "actionName":actionName, "params":params,"deviceId":deviceId}}
        payload = xacml_request_builder.buildRequest(bundle)
        
##        print("Debug in access_control.py : 38")
##        print("XACML Request : ")
##        print(payload)
        
        result = platform_manager.queryToPDP(payload)
        
        #mock up the value of result for testing
        result["decision"]=True
        
        if(result["decision"]):
            values = list(map(lambda p: p["value"], params))
            receive = device_manager.accessToDevice(deviceName, macAddress, actionName, values)
            receive = yaml.safe_load(receive)["result"] == "Success"
            result["success"]=receive #Whether the device is running successfully.
            
        print("Debug in access_control.py : 56")
        print(json.dumps(result))
            
    else:
        result = "{}"
    
    return json.dumps(result)