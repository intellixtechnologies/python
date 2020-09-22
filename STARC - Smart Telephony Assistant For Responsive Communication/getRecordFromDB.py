import sqlalchemy
import json
import datetime
# Set the following variables depending on your specific
# connection name and root password from the earlier steps:
connection_name = "silver-cairn-288316:us-central1:cardinal-data"
db_password = ""
db_name = "cardinaldb"

db_user = "pub"
driver_name = 'mysql+pymysql'
query_string = dict({"unix_socket": "/cloudsql/{}".format(connection_name)})


def getRecordFromDB(request):
    d , a = {} , []
    request_json = request.get_json()
    #phonenum = request_json['phone']
    if request.args and 'phone' in request.args:
        phonenum = request.args.get('phone')
    elif request_json and 'phone' in request_json:
        phonenum = request_json['phone']
    else:
        return 'No phone number received'

    print('Receivd phone number is ',phonenum)
    stmt = sqlalchemy.text("SELECT * FROM CUSTOMER where phone ="+phonenum+" and processed = 'N';")
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
      pool_timeout=30,
      pool_recycle=1800
    )
    try:

        with db.connect() as conn:
            results = conn.execute(stmt).fetchall()
            for result in results:
                print(result)
                for column, value in result.items():
                    if(column == 'CALL_BK_DT'):
                        t = value
                        date_ = t.strftime('%m/%d/%Y')
                        value = date_
                        
                    if(column == 'CALLBK_TIME'):
                        time_ = str(value)
                        value = time_
                        value = value.replace(":",".")

                    if(column == 'DATE_STMP'):
                        dt = value.strftime('%Y-%m-%d %H:%M:%S')
                        value = dt
                        value = value.replace(":",".")
                    if(column == 'PROCESSED'):
                        value = 'Y'
                    print("ColumnName:", column , "Value ", value)
                    d = {**d, **{column:value}}
                a.append(d)
            #c = results[0]
            # and now, finally...
            #dict_ = dict(zip(c.keys(), c.values()))
            sqlupdate = sqlalchemy.text("UPDATE CUSTOMER SET processed = 'Y' where phone ="+phonenum+" and processed = 'N';")
            
            try:
                with db.connect() as conn1:
                    res = conn1.execute(sqlupdate)
                print('Number of Rows where processed flag set as Y ', res.rowcount)         
            except Exception as e:
                return 'Error: {}'.format(str(e))
            
            return json.dumps(a)
    except Exception as e:
        return 'Error: {}'.format(str(e))
    return json.dumps(a)