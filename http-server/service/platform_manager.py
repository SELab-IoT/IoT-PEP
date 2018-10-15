from util import requester
import json
    
# 2. Device Registration
## Step 9
def updateDeviceProfiles(deviceProfiles):
    pepId = "pep_1" # TODO:Load from profile file.
    data = deviceProfiles
    response = requester.sendRequest(pepId, data, "POST");
    result = response.json()
    return result


# 4. Access Control
## Step 2
def queryToPDP(payload):
    response = requester.sendRequest("evaluate/", payload, "POST")
    raw = response.text
    
    def parseResponse():
        result = {}
        result["decision"] = "<Decision>Permit</Decision>" in raw
        
        # TODO: Improve handle advices later
        result["advices"] = []
        if "<Advices>" in raw:
            result["advices"].append(raw[raw.find("<Advices>"):raw.find("</Advices>")])
        return result
    
    result = parseResponse()
    return result

