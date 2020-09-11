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
        smsdelivered = reqdata['smsdelivered']
        print("fname: {}\n lname: {} \n phone: {}\n braodcaststatus: {}\n smsdelivered: {}\n params:{}".format(fname,lname,phone,status,smsdelivered,params))
    except:
        raise
    
    return (jsonify({"status":200, "fname":reqdata['fname'], "lname":reqdata['lname'],"phone":reqdata['phone'],"status":reqdata['broadcaststatus'],"smsdelivered":reqdata['smsdelivered'],"params":reqdata['params']}))
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5555)


