# Download the helper library from https://www.twilio.com/docs/python/install
from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/test", methods=['GET'])
def test():
    return jsonify({'status': 200})

@app.route("/callstatus", methods=['POST'])
def callstatus():
    #if not request.json:
    #    abort(400)
    reqdata = request.form
    print(request.form)
    try:
        
        fname = reqdata['fname']
        lname = reqdata['lname']
        phone = reqdata['phone']
        status = reqdata['broadcaststatus']
        params = reqdata['params']
        
        print("fname: {}\n lname: {} \n phone: {}\n braodcaststatus: {}\n params:{}".format(fname,lname,phone,status,params))
    except:
        raise
    #print(jsonify({"status":"call successful"}))
    return (jsonify({"status":200}))
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5555)


