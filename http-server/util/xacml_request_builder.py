import json

def buildRequest(bundle):
    
    prefix_type = "http://www.w3.org/2001/XMLSchema#"
    
    pepId = bundle["pepId"]
    body = bundle["body"]
    
    userId = body["userId"]
    deviceId = body["deviceId"]
    actionId = body["actionId"]
    params = body["params"]
    
    attributes = []
    for param in params:
        paramId = param["name"]
        paramValue = param["value"]
        paramType = prefix_type + param["type"]
        attribute = {
                        "id" : paramId,
                        "values" : [
                            {"type": paramType, "value":paramValue}
                        ]
                    }
        attributes.append(attribute)
    
    req = {
        "pepId":pepId,
        "body":[
            {
                "attributes":[
                    {
                        "id":"subject_id",
                        "values":[
                            {"type":prefix_type+"string", "value":userId}
                        ]
                    }
                ],
                "category":"subject"
            },
            {
                "attributes":[
                    {
                        "id":"resource_id",
                        "values":[
                            {"type":prefix_type+"string", "value":deviceId}
                        ]
                    }
                    
                ],
                "category":"resource"
            },
            {
                "attributes":[
                    {
                        "id":"action_id",
                        "values":[
                            {"type":prefix_type+"string", "value":actionId}
                        ]
                    }
                ],
                "category":"action"
            },
            {
                "attributes":attributes,
                "category":"params"
            }
        ]
        
    }
    
    return req
