from flask import Flask
from flask import request
from flask_mysqldb import MySQL

app = Flask(__name__)

#can get service address with $RELEASE-NAME{and then whatever}
app.config['MYSQL_HOST'] = '$RELEASE-NAME-service'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB'
mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/shutdown', methods=['POST'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/connect', methods=['GET'])
def connect():
    pass

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
