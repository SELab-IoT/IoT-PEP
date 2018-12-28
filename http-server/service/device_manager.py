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
    nearbyDevices = bluetooth.discover_devices(duration=6, lookup_names=True, flush_cache=True)
    for addr, name in nearbyDevices:
        discoverList[name] = addr
    scanList = discoverList
    print("Debug in device_manager.py:20")
    print(scanList)
    return discoverList


# 2. Device Registration
## Step 7
def connectToDevices(deviceList, scanList):

    def requestDeviceProfiles(deviceList, scanList): 
        deviceProfiles = []
        for deviceName in deviceList:
            print("Debug in device_manager.py:29")
            print(scanList)
            deviceProfile = connectToDevice(deviceName, scanList) #parameters missed ->scanList
            
            # Action Params to String - PlatformManager handle params to String only...
##            tmp = deviceProfile["actions"]
##            actions = []
##            for action in tmp:
##                action["params"] = str(action["params"])
##                actions.append(action["params"])
##            deviceProfile["actions"] = actions
            
            deviceProfiles.append(deviceProfile)
            
        return deviceProfiles            
    ####### change -> scanList.empty()
    if(scanList == None or len(scanList)==0):
        deviceProfiles = []
    else:
        deviceProfiles = requestDeviceProfiles(deviceList, scanList)

    print("Debug in device_manager.py:41")
    print(deviceProfiles)

    return deviceProfiles

def getDeviceProfile(deviceName,sock):
    sock.send("{ \"command\" : \"getProfile\"}")
    receiveData = sock.recv(1024)
    print("Debug in device_manager.py:46  : Received Data from Device")
    print(receiveData)
    sock.close()
    return receiveData
#    while True:
#        try:
#            receiveData = sock.recv(1024)
#            pinrt(receiveData)
#            if(receiveData != None):
#                #sock.close()
#                return receiveData
#        except Exception:
#            sock.close()
#            return None

def connectToDevice(deviceName, scanList):
    
    #print(deviceName)
    addr = scanList[deviceName]
    print("Connect To: "+addr)
    if addr != None:
        serviceMatches = bluetooth.find_service(name=deviceName, address=addr)
        if len(serviceMatches) == 0:
            #continue is not suitable
            #continue
            return
        firstMatch = serviceMatches[0]
        port = firstMatch["port"]
        name = firstMatch["name"]
        host = firstMatch["host"]
    #using device name and mac to find service    
    print("Connecting to device... : %s (host: %s)" % (name, host))
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((host, port))
    print("Connected!")  
    profile = getDeviceProfile(deviceName, sock)
    return yaml.safe_load(profile)


## Step 9
def updateDevices(profiles):
    response = platform_manager.updateDeviceProfiles(profiles)
    return response
    

# 4. Access Control
## Step 2 ~ 4
def accessToDevice(deviceName, macAddress, actionName, params):
    
    ## It's mockup code
    #deviceAddr = "B8:27:EB:7C:5A:B1"
    #deviceName = "aircon"
    
    # connect to device agian
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    serviceMatches = bluetooth.find_service(name = deviceName, address = macAddress)
    if len(serviceMatches) > 0:
        firstMatch = serviceMatches[0]
        port = firstMatch["port"]
        name = firstMatch["name"]
        host = firstMatch["host"]
    #using device name and mac to find service    
    #print("Connecting to device... : %s (host: %s)" % (name, host))
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((host, port))
        print("Connected!")
    
    #send the instruction
    print(eval(json.dumps(params)))
    instruction = {"actionName":actionName, "params":params}
    sock.send(json.dumps(instruction) )
    #time.sleep(1)
    response = sock.recv(1024)
    time.sleep(2)
    sock.close()
    
    return response

