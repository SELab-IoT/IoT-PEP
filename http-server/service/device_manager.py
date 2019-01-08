#-*- coding: utf-8 -*-

from service import platform_manager
import bluetooth
import json
import yaml
import time

scanList = {}

# 2. Device Registration
## Step 3
def scanDeviceList():
    global scanList
    discoverList = {}
    nearbyDevices = bluetooth.discover_devices(duration=5, lookup_names=True, flush_cache=True)
    for addr, name in nearbyDevices:
        discoverList[name] = addr
    scanList = discoverList
    return discoverList


# 2. Device Registration
## Step 7
def connectToDevices(deviceList, scanList):

    def requestDeviceProfiles(deviceList, scanList): 
        deviceProfiles = []
        for deviceName in deviceList:
            deviceProfile = connectToDevice(deviceName, scanList) 
            
            # TODO: Maybe Dead Code. remove later
            # Action Params to String - PlatformManager handle params to String only...
##            tmp = deviceProfile["actions"]
##            actions = []
##            for action in tmp:
##                action["params"] = str(action["params"])
##                actions.append(action["params"])
##            deviceProfile["actions"] = actions
            
            deviceProfiles.append(deviceProfile)
            
        return deviceProfiles
    
    if(scanList == None or len(scanList)==0):
        deviceProfiles = []
    else:
        deviceProfiles = requestDeviceProfiles(deviceList, scanList)

    return deviceProfiles


def getDeviceProfile(deviceName,sock):
    sock.send("{ \"command\" : \"getProfile\"}")
    # When Device have no profile, sock.recv(1024) not finishing...
    receiveData = sock.recv(1024)
    print("Debug in device_manager.py:46  : Received Data from Device")
    print(receiveData)
    sock.close()
    return receiveData


def connectToDevice(deviceName, scanList):    
    addr = scanList[deviceName]
    if addr != None:
        serviceMatches = bluetooth.find_service(name=deviceName, address=addr)
        if len(serviceMatches) == 0:
            return {}
        firstMatch = serviceMatches[0]
        port = firstMatch["port"]
        name = firstMatch["name"]
        host = firstMatch["host"]
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((host, port))
    profile = getDeviceProfile(deviceName, sock)
    
    return yaml.safe_load(profile)


## Step 9
def updateDevices(profiles):
    return platform_manager.updateDeviceProfiles(profiles)
    

# 4. Access Control
## Step 2 ~ 4
def accessToDevice(deviceName, macAddress, actionName, params):
    
    # connect to device agian
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    serviceMatches = bluetooth.find_service(name = deviceName, address = macAddress)
    if len(serviceMatches) > 0:
        firstMatch = serviceMatches[0]
        port = firstMatch["port"]
        name = firstMatch["name"]
        host = firstMatch["host"]
        
        #using device name and mac to find service
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((host, port))
        
    #Send the Action Command
    print(eval(json.dumps(params)))
    instruction = {"actionName":actionName, "params":params}
    sock.send(json.dumps(instruction))
    
    response = sock.recv(1024)
    time.sleep(2)
    sock.close()
    
    return response

