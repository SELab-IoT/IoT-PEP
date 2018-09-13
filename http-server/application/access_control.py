from application import app
from service import device_manager, platform_manager
from util import session_manager, xacml_request_builder
import json
from flask import request

# 4. Access Control(XACML Request)
## 1. Device Access Request
## ~ 4. Return Permit or Deny
@app.route("/devices/<deviceId>", methods=['POST'])
def requestForAccessToDevice(deviceId):
    
    def parseRequest():
        content = request.get_json()
        actionId = content.get("actionId")
        actionName = content.get("actionName")
        params = content.get("params")
        return (actionId, actionName, params)
    
    pepId = "pep_1" # TODO: remove hardcode -> replace it read profile file.
    userId = session_manager.get("userId")
    userId = "frebern" # Debug
    
    actionId, actionName, params = parseRequest()
    
    bundle = {"pepId":pepId, "body":{"userId":userId, "deviceId":deviceId, "actionId":actionId, "actionName":actionName, "params":params}}
    payload = xacml_request_builder.buildRequest(bundle)
    result = platform_manager.queryToPDP(payload)
    
    if(result["decision"]):
        values = list(map(lambda p: p["value"], params))
        device_manager.accessToDevice(action, values)
    
    return json.dumps(result)