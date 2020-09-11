import requests
import json
endpoint_url="https://kit.voximplant.com/api/v3/scenario/runScenario" #RunSCenario

request_parameters =  dict()
fname = "John" #customer fname
lname = "Rambo" #customer lname
# Max variable/param length for vox is 255. 
# So need to split between custommsg 1 and 2 if more than 255. Else send a " " for custommsg1. Don't send a Null.
custommsg = "With the Flu season just round the corner, Cardinal Health is happy to announce that we are ready with your Flu shots. You can now pre-order the flu shots and book an appointment for your entire family from our website or by visiting your nearest pharmacy."
custommsg1= "Our customer executives will be happy to assist you with more details on the overall booking process, offers and pricing. Would you like to hear back from one of our representatives? You may say Yes to schedule a call or No to disconnect."
smstext = "Cardinal Health is ready with your Flu shots. We will call you soon with more details."
request_parameters["phone"]="918017777750" #customer phone number
request_parameters["phone_number_id"]="1853"
request_parameters["scenario_id"]="15682"
request_parameters["variables"]=json.dumps({"fname":fname,"lname":lname,"broadcaststatus":"N","custommsg":custommsg,"custommsg1":custommsg1,"smstext":smstext,"smsdelivered":"N"})
request_parameters["domain"]="tcs"
request_parameters["access_token"]="79b33f8548b585bb93c51e3af9adbfa1"

print(request_parameters)

resp=requests.post(url=endpoint_url,data=request_parameters)

print(resp.status_code)
print(resp.text) #Only status of this call will be received. For Details around the call, check the flask API