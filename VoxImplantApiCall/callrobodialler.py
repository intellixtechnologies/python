import requests
import json

VOX_url="https://us-central1-silver-cairn-288316.cloudfunctions.net/VoxAPICall"
DB_url = "https://us-central1-silver-cairn-288316.cloudfunctions.net/pollDB-v1"


def callRobodialler(request):
    apikey='STARC09172020'
    dict_ = {"phone_number":"", 
    "broadcast_msg":"",
    "smstext":"",
    "customer_fname":"",
    "customer_lname":""}
    dbdict = {"phone":""}
    print('Received call in  method callRobodialler..\n')
    request_json = request.get_json()
    if (not(request_json) or (request_json['access_key']!=apikey)):
        return 'Access denied'
    if (request_json) and ('phone_number' in request_json) and ('broadcast_msg' in request_json) and ('smstext' in request_json) and ('customer_fname' in request_json) and ('customer_lname' in request_json):
        dict_["phone_number"] = request_json['phone_number']
        dbdict["phone"] = request_json['phone_number']
        dict_["broadcast_msg"] = request_json['broadcast_msg']
        dict_["smstext"] = request_json['smstext']
        dict_["customer_fname"] = request_json['customer_fname']
        dict_["customer_lname"] = request_json['customer_lname']

        if (len(dict_["phone_number"]) == 0):
            return 'Phone number is invalid'
        if (len(dict_["broadcast_msg"]) == 0):
            return 'Broadcast Message is invalid'
        if( len(dict_["smstext"]) == 0):
            return 'SMS Text is invalid'
        if (len(dict_["customer_fname"]) == 0 and len(dict_["customer_lname"])==0):
            return 'Customer name details invalid'
        print('Calling VOX..\n')
        VOXresponse = requests.post(VOX_url, json=dict_)
        print("VOX Call Status code: ", VOXresponse.status_code)
        if (VOXresponse.status_code == 200 ):
            print('Response received from VOX ...\n',VOXresponse.json())
            print('\nPolling DB to get status ...\n')
            DBresponse = requests.post(DB_url, json=dbdict)
            print("DB Call Status code: ", DBresponse.status_code)
            if (DBresponse.status_code == 200 ):
                
                print('Response received from DB ...\n',DBresponse.json())
                return(DBresponse.json())
            else:
                print("Failed calling DB URL")
                return(json.dumps("Failed calling DB URL"))


        else:
            print("Failed calling VOX. Required elements missing")
            return(json.dumps("Failed calling VOX. Required elements missing"))
