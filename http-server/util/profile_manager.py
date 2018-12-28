#-*- coding: utf-8 -*-
import json
import yaml

profile = {}

# load Profile (default path : resources/profile/pep.profile)
# base is server.sh
def loadProfile(base = "resources/profile/", file = "pep.profile"):
    global profile
    fo = open(base+file,"r")
    stringProfile = fo.read() #read all information
    tmp = json.loads(stringProfile)
    tmp = json.dumps(tmp)
    tmp = yaml.safe_load(tmp)
    profile = tmp["profile"] #split the pep profile as dict type
    print(profile)
    fo.close()
    

# return profile as string
def getProfileAsString():
    return json.dumps(profile)

def getProfileAsDict():
    return profile

# return pepId
def getPEPId():
    return profile["pepId"]
