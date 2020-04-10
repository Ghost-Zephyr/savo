from werkzeug.exceptions import HTTPException
from flask_pymongo import PyMongo
from flask import Flask, jsonify, request

from game import api, jwt #, admin

# ----- App init -----
app = Flask(__name__)
jwt.keypair = jwt.set_keypair(jwt.read_keyfiles())

app.config['MONGO_DBNAME'] = 'savo'
app.config['MONGO_URI'] = 'mongodb://mongodb:27017/savo'
mongo = PyMongo(app)
db = mongo.db

# ----- Routes -----
app.add_url_rule('/', 'index', api.index, methods=['GET', 'BREW'])
app.add_url_rule('/user', 'user', api.user, defaults={ 'db': db, 'token': jwt.get() }, methods=['GET'])
app.add_url_rule('/register', 'register', api.register, defaults={ 'db': db }, methods=['POST'])
app.add_url_rule('/login', 'login', jwt.login, defaults={ 'db': db }, methods=['POST'])
app.add_url_rule('/logout', 'logout', jwt.logout, methods=['GET', 'POST'])

@app.errorhandler(Exception)
def handleError(err): # game/__init__.py do some funky lol in production?
    if isinstance(err, HTTPException):
        return err
    return 'Internal Server Error', 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8060)

