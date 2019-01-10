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
        actionId = content.get("actionId")
        actionName = content.get("actionName")
        params = content.get("params")
        deviceName = content.get("deviceName")
        macAddress = content.get("macAddress")
        userId = content.get("userId")
        sessionKey = content.get("sessionKey")
        return (userId, sessionKey, actionId, actionName, params, deviceName, macAddress)
    
    pepId =  profile_manager.getPEPId()
    userId, sessionKey, actionId, actionName, params, deviceName, macAddress = parseRequest()
    loggedIn = session_manager.checkLogin(userId, sessionKey)
    
    if(loggedIn):
        bundle = {"pepId":pepId, "body":{"userId":userId, "deviceName":deviceName, "actionId":actionId, "actionName":actionName, "params":params,"deviceId":deviceId}}
        payload = xacml_request_builder.buildRequest(bundle)
        result = platform_manager.queryToPDP(payload)
        if(result["decision"]):
            values = list(map(lambda p: p["value"], params))
            # Is device running successfully?
            receive = device_manager.accessToDevice(deviceName, macAddress, actionName, values)
            receive = yaml.safe_load(receive)["result"] == "Success"
            result["success"]=receive
        else:
            result["success"]=False
    else:
        result = {}
    
    return json.dumps(result)

