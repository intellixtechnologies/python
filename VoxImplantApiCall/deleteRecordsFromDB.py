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


def deleteRecordFromDB(request):
    dict_={'Result':'Failed', 'RowsDeleted':0}
    if request.method == 'DELETE'and 'phone' in request.args:
        phonenum = request.args.get('phone')
        print('phone number to delete is', phonenum)
        stmt = sqlalchemy.text('DELETE FROM CUSTOMER where phone ='+phonenum+';')
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
                results = conn.execute(stmt)
                print('number of rows affected ', results.rowcount)
                dict_['Result'] = "Success"
                dict_['RowsDeleted'] = results.rowcount
                return json.dumps(dict_)
        except Exception as e:
            dict_['Result'] = "Failed"
            print(str(e))
            return json.dumps(dict_)

        
    else:
        return json.dumps(dict_)
