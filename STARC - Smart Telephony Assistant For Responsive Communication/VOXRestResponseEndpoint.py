from flask import jsonify
import sqlalchemy
from datetime import datetime
import json
def main(request):
    
    #reqdata = request.form
    reqdata = request.form.to_dict()
    print(reqdata)
    #try:

    #default values 
    custommsg = ""
    custommsg1 = ""
    cust_callbk= ""
    time = "00:00:00"
    date = "0000-00-00"
    message = ""
    custom_msg_yn = ""
    #time_stmp = "0000-00-00 00:00:00"
    sms_txt = ""
    
    fname = reqdata['fname']
    lname = reqdata['lname']
    phone = reqdata['phone']
    status = reqdata['broadcaststatus']
    params_str = reqdata['params']
    params = json.loads(params_str)
    smsdelivered = reqdata['smsdelivered']
    if "smstext" in reqdata:
        sms_txt = reqdata["smstext"] 
    print("smstext: {}".format(sms_txt))
    #params values
    if "custommsg" in params:
        custommsg = params["custommsg"]
    if "custommsg1" in params:            
        custommsg1 = params["custommsg1"]
    if "cust_callbk" in params:
        cust_callbk= params["cust_callbk"]
    if "time" in params:
        time_raw = params["time"]
    if "date" in params:
        date_raw = params["date"]        
    if "message" in params:
        message = params["message"]
    if "custom_msg_yn" in params:
        custom_msg_yn = params["custom_msg_yn"]        

    time_stmp = datetime.now()
    date_raw = date_raw.strip()
    date = (date_raw.split('T'))[0]

    time_raw = time_raw.strip()
    time = (time_raw.split('T')[1]).split('+')[0]
    print("custommsg: {}\n custommsg1: {} \n cust_callbk: {}\n time: {}\n date: {}\n message:{}\n custom_msg_yn: {}\n sms_txt: {}\n time_stmp:{}".format(custommsg,custommsg1,cust_callbk,time,date,message,custom_msg_yn,sms_txt,time_stmp))


    print("fname: {}\n lname: {} \n phone: {}\n braodcaststatus: {}\n smsdelivered: {}\n params:{}".format(fname,lname,phone,status,smsdelivered,params))
    #except:
    #    raise
    
    #return (jsonify({"status":200, "fname":reqdata['fname'], "lname":reqdata['lname'],"phone":reqdata['phone'],"status":reqdata['broadcaststatus'],"smsdelivered":reqdata['smsdelivered'],"params":reqdata['params']}))
    #sqlpart starts here

    # Set the following variables depending on your specific
    # connection name and root password from the earlier steps:
    connection_name = "silver-cairn-288316:us-central1:cardinal-data"
    db_password = ""
    db_name = "cardinaldb"

    db_user = "pub"
    driver_name = 'mysql+pymysql'
    query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})
    
    #stmt = sqlalchemy.text("insert into CUSTOMER (PHONE,FNAME,LNAME) VALUES (:a, :b, :c)")
    #stmt = sqlalchemy.text("insert into CUSTOMER (PHONE,FNAME,LNAME,BRDCST_MSG,BRDCST_MSG1,SMS_TEXT,BRDCST_CMPLT,SMS_YN,CUST_CALLBK,CALL_BK_DT,CALLBK_TIME,CUSTOM_MSG_YN,CUSTOM_MSG,DATE_STMP).\
	#                   VALUES (:a, :b, :c,:d,:e,:f,:g,:h,:i,:j,:k,:l,:m,:n)")
    
    stmt = sqlalchemy.text("insert into CUSTOMER (PHONE,FNAME,LNAME,BRDCST_MSG,BRDCST_MSG1,SMS_TEXT,BRDCST_CMPLT,SMS_YN,CUST_CALLBK,CUSTOM_MSG_YN,CUSTOM_MSG,DATE_STMP,CALL_BK_DT,CALLBK_TIME) VALUES (:a, :b, :c, :d, :e, :f, :g, :h, :i, :j, :k, :l, :m, :n);")
    

    #stmt = sqlalchemy.text('delete from response where fname="trump";')
    
    db = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
        drivername=driver_name,
        username=db_user,
        password=db_password,
        database=db_name,
        query=query_string,
    ),
    pool_size=5,
    max_overflow=2,
    pool_timeout=60,
    pool_recycle=1800
    )
    try:
        with db.connect() as conn:
            res = conn.execute(stmt,a=phone, b=fname, c=lname, d=custommsg, e=custommsg1, f=sms_txt, g=status, h=smsdelivered, i=cust_callbk, j=custom_msg_yn, k=message, l=time_stmp, m=date, n=time)
            conn.commit()
            print(res)         
    except Exception as e:
        return 'Error: {}'.format(str(e))
    return 'Process Successful'