import requests
import json
endpoint_url="https://kit.voximplant.com/api/v3/scenario/runScenario" #RunSCenario

request_parameters =  dict()
fname = "Abhishek" #customer fname
lname = "Roy" #customer lname
request_parameters["phone"]="918017777750" #customer phone number
request_parameters["phone_number_id"]="1853"
request_parameters["scenario_id"]="15682"
request_parameters["variables"]=json.dumps({"fname":fname,"lname":lname,"broadcaststatus":"N"})
request_parameters["domain"]="tcs"
request_parameters["access_token"]="79b33f8548b585bb93c51e3af9adbfa1"

print(request_parameters)

resp=requests.post(url=endpoint_url,data=request_parameters)

print(resp.status_code)
print(resp.text) #Only status of this call will be received. For Details around the call, check the flask API