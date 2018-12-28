#-*- coding: utf-8 -*-

from datetime import datetime, date, time, timedelta
from util import requester
from application import app

userList = {}

def login(userId, sessionKey):
    
    global userList
    
    SUCCEED = "{\"login\":true}"
    FAILED = "{\"login\":false}"
    
    isValidSessionKey = checkSessionKeyValidity(userId, sessionKey)
    if(isValidSessionKey):
        timestamp = datetime.now().time()
        userList[userId] = {"sessionKey":sessionKey, "timestamp":timestamp}
        return SUCCEED
    else:
        return FAILED
    
# Session Check
def checkSessionKeyValidity(userId, sessionKey):
    result = queryToPlatformManager(userId, sessionKey)
##    result = True #for test
    return result
    
def logout(userId, sessionKey):
    global userList
    if(checkLogin(userId, sessionKey)):
        del userList[userId]
        
# Use this when a app.route function needs to be logged in
def checkLogin(userId, sessionKey):
    global userList
    sKey = userList[userId]["sessionKey"]
    ts = userList[userId]["timestamp"]
    return sKey == sessionKey and isExpired(ts)

def isExpired(timestamp):
    now = datetime.now().time()
    past = timestamp
    expire = timedelta(hours=1)
    return (datetime.combine(date.today(), past)+expire).time() > now

# Query "is this valid sessionKey?" to Platform Manager
def queryToPlatformManager(userId, sessionKey):
    content = {}
    content["userId"] = userId
    content["sessionkey"] = sessionKey
    result = requester.sendRequest("session", payload, "POST")
    return result["authenticated"]
    