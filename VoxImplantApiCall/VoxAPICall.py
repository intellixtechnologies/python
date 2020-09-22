import requests
import json
import time
from flask import jsonify
def hello_world(request):

    #file = request.files['file']
    
    #fileData=file.read()
    #parsed = json.loads(fileData)

    parsed = request.get_json(force=True)
    
    msg = parsed["broadcast_msg"]
    if(len(msg)>255):
        custmsg = msg[0:254]
        custmsg1 = msg[255:len(msg)]
    else:
        custmsg = msg
        custmsg1 = ' '

    endpoint_url="https://kit.voximplant.com/api/v3/scenario/runScenario" #RunSCenario
    request_parameters =  dict()

    request_parameters["phone"]=parsed["phone_number"] #customer phone number
    request_parameters["phone_number_id"]="1853"
    request_parameters["scenario_id"]="15682"
    request_parameters["variables"]=json.dumps({"fname":parsed["customer_fname"],"lname":parsed["customer_lname"],"broadcaststatus":"N","custommsg":custmsg,"custommsg1":custmsg1,"smstext":parsed["smstext"],"smsdelivered":"N"})
    request_parameters["domain"]="tcs"
    request_parameters["access_token"] = "79b33f8548b585bb93c51e3af9adbfa1"


    print(request_parameters)

    resp=requests.post(url=endpoint_url,data=request_parameters)

    time.sleep(10)


    print(resp.status_code)
    print(resp.text) #Only status of this call will be received. For Details around the call, check the flask API
    
    return(json.loads(resp.text))
    #return(jsonify({"result":resp.text}))       
