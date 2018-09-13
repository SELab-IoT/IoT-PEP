from flask import session
from util import requester
from application import app

app.secret_key = "default secret key"

def login(userId, sessionKey):
    
    app.secret_key = sessionKey
    
    SUCCEED = "{\"login\":true}"
    FAILED = "{\"login\":false}"
    
    # TODO: Uncomment below later(When Platform Manager implements login, session)
##    isValidSessionKey = checkSession(userId, sessionKey)
##    if(isValidSessionKey):
##        makeSession(userId)
##        return SUCCEED
##    else return FAILED
    
    # TODO: And remove below 2 lines later
    makeSession(userId)
    return SUCCEED

def logout():
    if(isLoggedIn()):
        clearSession()

def isLoggedIn():
    return 'userId' in session

# Session Check
# TODO: Change Valid Session Key message later.
def checkSession(userId, sessionKey):
    result = queryToPlatformManager(userId, sessionKey)
    return result

# Query "is this valid sessionKey?" to Platform Manager
def queryToPlatformManager(userId, sessionKey):
    content = {}
    content["userId"] = userId
    content["sessionkey"] = sessionKey
    result = requester.sendRequest("session", payload, "POST")
    return result["authenticated"]

# Create a session for user
def makeSession(userId):
    session["userId"] = userId
    
def clearSession():
    session.clear()
    
def putInSession(key, value):
    session[key] = value

def get(key):
    return session[key] if key in session else None
