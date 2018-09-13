from service import platform_manager
import bluetooth

# 2. Device Registration
## Step 3
def scanDeviceList():
    discoverList = {}
    nearbyDevices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True)
    for addr, name in nearbyDevices:
        discoverList[name] = addr
    return discoverList


# 2. Device Registration
## Step 7 ~ 9
def connectToDevices(deviceList, scanList):

    ### Step 7
    def requestDeviceProfiles(deviceList, scanList): # This is not a pure function. don't move this outside.
        
        deviceProfiles = []
        
        for deviceName in deviceList:        
            addr = scanList[deviceName]
            if addr != None:
                serviceMatches = bluetooth.find_service(address=addr)
                if len(serviceMatches) == 0:
                    continue
                firstMatch = serviceMatches[0]
                port = firstMatch["port"]
                name = firstMatch["name"]
                host = firstMatch["host"]
                
            print("Connecting to device... : %s (port: %s)" % (name, host))
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((host, port))
            print("Connected!")
            
            profile = getDeviceProfile(deviceName, sock)
            deviceProfiles.append(profile)
            
        return deviceProfiles            

    ### Step 7.1.
    def getDeviceProfile(sock):
        sock.send("{ \"command\" : \"getProfile\"")
        while True:
            try:
                receiveData = sock.recv(1024)
                if(receiveData != None):
                    sock.close()
                    return receiveData
            except Exception:
                sock.close()
                return None
        
    deviceProfiles = requestDeviceProfiles()
    isAuthenticated = platform_manager.updateDeviceProfiles(deviceProfiles)
    
    # Debug
    if not isAuthenticated["authenticated"]:
        print(device + " can't update profile")
        
    return isAuthenticated

# 4. Access Control
## Step 2 ~ 4
def accessToDevice(action, params):
    pass

