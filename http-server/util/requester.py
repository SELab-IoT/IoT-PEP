import requests
import json

# Send Request to PlatformManager
PLATFORM_MANAGER = "http://selab.hanyang.ac.kr:8080/"

# send request to PM
def sendRequest(subURL, content, method="GET"):
    result = None
    URL = PLATFORM_MANAGER + subURL
    if(method == "GET"):
        result = sendGetRequest(URL, content)
    elif(method == "POST"):
        result = sendPostRequest(URL, content)
    return result

# send get request to PM
def sendGetRequest(url, content):
    return requests.get(url, params=content)

# send post request to PM
def sendPostRequest(url, content):
    return requests.post(url, data=json.dumps(content))
