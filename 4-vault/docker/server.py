from flask import Flask
from flask import request
from flask_mysqldb import MySQL
import mysql.connector
from  mysql.connector import errorcode
import os

app = Flask(__name__)

release_name = os.environ['RELEASE_NAME']
mysql_host = release_name+"-mysql"
mysql_root_user = os.environ['MYSQL_ROOT_USER']
mysql_root_password = os.environ['MYSQL_ROOT_PASSWORD']

config = {
  'user': mysql_root_user,
  'password': mysql_root_password,
  'host': mysql_host,
  'database': 'test',
  'raise_on_warnings': True
}



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/shutdown', methods=['POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/test_db', methods=['GET'])
def connect():
    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        print(cnx.connection_id)
        cursor.execute("SHOW TABLES")
        print(cursor.fetchall())
        cursor.execute("SHOW DATABASES")
        print(cursor.fetchall())
        cursor.execute("SELECT DATABASE()")
        print(cursor.fetchall())
        try:
            cursor.execute("SELECT 1 FROM testTable LIMIT 1")
        Except exception as e:
            print("no table yet")
            cursor.execute("CREATE TABLE testTable (testID int)")
        print(cursor.fetchall())
        #DOES THIS WORK!?!? - seems to but untested on actual cluster
        #but wtf am I even returning. I won't get any feedback here. 
        cursor.execute("SHOW TABLES")
        print(cursor.fetchall())


        cursor.execute("INSERT INTO testTable (testID) VALUES (1)")
        cursor.execute("SELECT * FROM testTable")
        print(cursor.fetchall())
        print(cursor.fetchall())
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
