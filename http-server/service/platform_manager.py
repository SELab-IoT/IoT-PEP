#-*- coding: utf-8 -*-

from util import requester
import json
from util import profile_manager
    
# 2. Device Registration
## Step 9
def updateDeviceProfiles(deviceProfiles):
    pepId = profile_manager.getPEPId()
    data = deviceProfiles
    response = requester.sendRequest("devices/"+pepId, data, "POST");
    return response.json()


# 4. Access Control
## Step 2
def queryToPDP(payload):

    raw = response.textrequester.sendRequest("evaluate/", payload, "POST").text
    
    def parseResponse():
        result = {}
        result["decision"] = "<Decision>Permit</Decision>" in raw
        
        # TODO: Improve handle advices later
        result["advices"] = []
        if "<Advices>" in raw:
            result["advices"].append(raw[raw.find("<Advices>"):raw.find("</Advices>")])
        return result
    
    return parseResponse()


