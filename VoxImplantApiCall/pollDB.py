import requests
import json
import time

def pollDB(request):
    dict_ = {"phone":""}
    finalResp = {"RowsFound":"N"}
    sleepTime = 30
    def checkDB(count):
        print('\nreached check DB. Count is ', count , '\ndict is ', dict_)
        if (count == 0):
            print("No Records found.")
            return finalResp
        else: 
            print('Calling DB')
            response = requests.post(endpoint_url, json=dict_)

            if len(response.json()) == 0: 
                print('Going to sleep for ', sleepTime , ' seconds')
                time.sleep(sleepTime)
                return checkDB(count-1)
            else:
                print("One record found")
                finalResp["RowsFound"] = "Y" 
                newDict = response.json()[0]
                finalResp.update(newDict)
                return finalResp
    endpoint_url="https://us-central1-silver-cairn-288316.cloudfunctions.net/getRecordFromDB-v1"
    
    request_json = request.get_json()

    phonenum = request_json['phone']
    print('Received phone number is ',phonenum)

    dict_['phone'] = phonenum
    status = checkDB(10)
    print('Success')
    print('response is \n',status)
    
    return(json.dumps(status))


    #print("Printing Entire Post response")
    #print(response.json())
