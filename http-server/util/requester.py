#-*- coding: utf-8 -*-

import requests
import json
import yaml

# Send Request to PlatformManager
PLATFORM_MANAGER = "http://selab.hanyang.ac.kr:8080/"

# send request to PM
def sendRequest(subURL, content, method="GET"):
    result = None
    URL = PLATFORM_MANAGER + subURL
    
    print("-------------------------------------------------")
    print("* URL : "+URL + " ("+method+")")
    print("*** Content ***")
    print(content)
    print("-------------------------------------------------")
    
    if(method == "GET"):
        result = sendGetRequest(URL, content)
    elif(method == "POST"):
        result = sendPostRequest(URL, content)
        
    print("*** Response ***")
    print(result)
    print("-------------------------------------------------")
        
    return result

# send get request to PM
def sendGetRequest(url, content):
    return requests.get(url, params=content)

# send post request to PM
def sendPostRequest(url, content):
    headers = {'content-type': 'application/json'}
    return requests.post(url, headers=headers, data=json.dumps(content))
