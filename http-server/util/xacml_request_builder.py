#-*- coding: utf-8 -*-
import json

def buildRequest(bundle):
    
    stringType = toXACMLType("string")
    
    pepId = bundle["pepId"]
    body = bundle["body"]
    
    userId = body["userId"]
    deviceId = body["deviceId"]
    actionId = body["actionId"]
    params = body["params"]
    
    attributes = []
    for param in params:
        paramId = param["name"]
        prefix, type = toXACMLType(param["type"])
        paramType = prefix+type
        paramValue = toXACMLLiteral(param["value"], type)
        
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
                            {"type":stringType, "value":userId}
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
                            {"type":stringType, "value":deviceId}
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
                            {"type":stringType, "value":actionId}
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

# Refer XACML 3.0 docs, 10.2.7 Data-types section.
def toXACMLType(raw):
    #Mapper for raw type to XACML type
    mapper = {
    
        "http://www.w3.org/2001/XMLSchema#":{
        
            "string":["String", "str"],
            "boolean":["Boolean", "Bool", "BOOL", "BOOLEAN", "bool"],
            "integer":["Integer","INTEGER","Int","INT","int","Long","long","LONG"],
            "double":["Double","DOUBLE","double","float", "Float", "FLOAT"],
            "time":["Time", "TIME"],
            "date":["Date", "DATE"],
            "dateTime":["DateTime", "DATETIME", "datetime", "Datetime"],
            "dayTimeDuration":["DayTimeDuration", "daytimeDuration"],
            "yearMonthDuration":["YearMonthDuration","yearmonthDuration"],
            "anyURI":["URI","Uri","uri","URL","Url","url","URN","Urn","urn","AnyURI","AnyURL","AnyURN","AnyUri","AnyUrl","AnyUrn","anyURL","anyURN","anyUri","anyUrl","anyUrn"],
            "hexBinary":["hex","HEX","Hex","HexBinary","HEXBinary"],
            "base64Binary":["Base64","BASE64","base64","Base64Binary","BASE64Binary"]
        
        },
        "urn:oasis:names:tc:xacml:1.0:data-type:":{
            "rfc822Name":["RFC822","rfc822","Rfc822","RFC822Name","Rfc822Name"],
            "x500Name":["X500","x500","X500Name"]
        },
        "urn:oasis:names:tc:xacml:3.0:data-type:":{
            "xpathExpression":["XpathExpression","XPathExpression","xPathExpression","xpath","xPath","XPath","Xpath"]
        },
        "urn:oasis:names:tc:xacml:2.0:data-type:":{
            "ipAddress":["ip","Ip","IP","IPAddress","IpAddress"],
            "dnsName":["dns","DNS","DNSName","Dns","DnsName"]
        }
        
    }
    
    #Traverse mapper to convert raw type to XACML type.
    for prefix, types in mapper:
        if(raw in types.keys()):
            return (prefix, raw)
        for xacmlType, rawTypes in types:
            if(raw in rawTypes):
                return (prefix, xacmlType)
            
    return ("", raw)
    
    
def toXACMLLiteral(type, raw):
    #Mapper for raw literal to XACML literal
    mapper = {
        "boolean":{
            "True" : ["true", "TRUE"],
            "False" : ["false", "FALSE"]
        }
    }
    
    # if mapper not define list for the type
    if not(type in mapper.keys()):
        return raw
    
    #Traverse mapper to convert raw value literal to XACML literal
    for xacml, raws in mapper[type]:
        if(raw in raws):
            return xacml
    
    return raw
    
    
    
    
