from flask import request, jsonify
from .users import *

def index():
    if request.method == 'BREW':
        res = jsonify('short and stout')
        res.status_code = 418
        return res
    else:
        return jsonify('1337 game API!')

