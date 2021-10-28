import json

def v3tov1(payload):
    if type(payload) == dict:
        props = [{"property":k, "value":v} for k, v in payload['properties'].items()]
        properties = {"properties":props}
        return properties
    if type(payload) == list:
        lst = []
        for record in payload:
            props = []
            for k, v in record['properties'].items():
                props.append({"property":k, "value":v})
            lst.append({"properties":props})
        return lst

def v1tov3(payload):
    if type(payload) == dict:
        props = {}
        for properties in payload["properties"]:
            props[properties['property']] = properties['value'] 
        properties = {"properties":props}
        return properties
    if type(payload) == list:
        lst = []
        for record in payload:
            props = {}
            for properties in record["properties"]:
                props[properties['property']] = properties['value'] 
            properties = {"properties":props}
            lst.append(props)
        return lst

# fi = open('v1properties.json', 'r')
# f = json.load(fi)
# v1tov3(f)