from bcrypt import hashpw, gensalt
from flask import jsonify, request
from ..jwt import createToken

def register(db):
    if request.json: json = request.json
    elif request.form: json = request.form
    else:
        o = jsonify('Invalid request.')
        o.status_code = 400
        return o
    if db.users.find_one({ 'nick': json['nick'] }):
        res = make_response("Nick taken.")
        res.status_code = 409
        return res
    try:
        if json['pwd'] != json['pwd1']:
            res = make_response("Passwords doesn't match!")
            res.status_code = 406
            return res
    except KeyError:
        pass
    db.users.insert_one({
        'nick': json['nick'],
        'email': json['email'],
        'pwd': hashpw(json['pwd'].encode('utf-8'), gensalt()),
        'superadmin': False,
        'admin': False,
        'pvestats': {},
        'pvpstats': {},
        'game': {},
        'deck': {},
        'collection': {}
    })
    token = createToken(db, json['nick'])
    resp = make_response(token)
    resp.set_cookie("jwt", token, max_age=60*60*24*7)
    return resp

def user(db, token):
    if request.json: json = request.json
    elif request.form: json = request.form
    else: json = {}
    users = db.users
    if token['admin'] and not json['nick']:
        o = {}
        for user in users.find():
            o[str(user["_id"])] = {
                "nick": user["nick"],
                "roles": user["roles"],
            }
        o = jsonify(o)
        return o
    elif json['nick']:
        user = users.find_one({ "nick": json['nick'] })
        if user:
            o = {
                "nick": user["nick"],
                "roles": user["roles"]
            }
            o = jsonify(o)
            o.status_code = 200
        else:
            o = "Could not find user."
            o = jsonify(o)
            o.status_code = 404
    elif not token['admin'] and json['nick'] != token['nick']:
        o = jsonify('Fuck off!')
        o.status_code = 403
    else:
        o = jsonify('Not logged in.')
        o.status_code = 401
    return o

