import requests
endpoint_url="https://kit.voximplant.com/api/v3/scenario/runScenario" #RunSCenario
#endpoint_url="https://kit.voximplant.com/api/v3/scenario/searchScenarios" #ScenarioID
#endpoint_url="https://kit.voximplant.com/api/v3/phone/searchNumbers" #Search PhoneNumberID
#endpoint_url="https://kit.voximplant.com/api/v3/callerid/searchCallerIDs" #Search CallerID

request_parameters =  dict()

#request_parameters["caller_id"]=0
request_parameters["phone"]=918017777750
request_parameters["phone_number_id"]=1853
request_parameters["scenario_id"]=15682
#request_parameters["variables"]={"fname":fname,"lname":lname}

request_parameters["domain"]="tcs"
request_parameters["access_token"]="79b33f8548b585bb93c51e3af9adbfa1"

print(request_parameters)
#resp=requests.get(url=endpoint_url,params=request_parameters)
resp=requests.post(url=endpoint_url,params=request_parameters)
print(resp.status_code)
print(resp.text)