from datetime import datetime, timedelta
from flask import request, make_response, redirect
from bcrypt import checkpw
from authlib.jose import jwt
import bcrypt
keypair = {}

# ----- JWT stuff -----
def set_keypair(keys):
    keypair = {
        'private': keys[0],
        'public': keys[1]
    }
    return keypair

def read_keyfiles(): # Binary read?
    try:
        prvkf = open("secret/jwt-keys/key.pem", "r")
        pubkf = open("secret/jwt-keys/key.pub", "r")
        b = prvkf.read(1)
        private_key = b
        while b != "":
            b = prvkf.read(1)
            private_key += b
        b = pubkf.read(1)
        public_key = b
        while b != "":
            b = pubkf.read(1)
            public_key += b
    except:
        print("\033[3mCould not read key files!\033[0m")
        exit()
    finally:
        prvkf.close()
        pubkf.close()
    return private_key, public_key

def createToken(db, nick):
    p = db.p.find_one({ "nick": nick })
    exp = datetime.utcnow() + timedelta(days=7)
    token = jwt.encode({'alg': 'RS256'}, {
        'nick': p['nick'],
        'admin': p['admin'],
        'exp': exp,
    }, keypair['private'])
    return token

def get():
    try:
        dec = jwt.decode(request.cookies.get('jwt'), keypair['public'])
        dec.validate()
        return dec
    except:
        return False

# ----- Flask stuff -----
def login(db):
    json = request.json if request.json else request.form
    p = db.p.find_one({ "nick": json['nick'] })
    if bcrypt.checkpw(json['pwd'].encode('utf-8'), p['pwd']):
        token = createToken(db, json['nick'])
        res = make_response("Token created.")
        res.set_cookie("jwt", token, max_age=60*60*24*7)
        return res
    else:
        res = make_response("Wrong password!")
        res.status_code = 401
        return res

def logout():
    res = make_response("Logged out.")
    res.set_cookie("jwt", "", max_age=0)
    return res
