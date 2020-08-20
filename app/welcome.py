from flask import request

from .utils import response
from .db_setup import add_db_odds, get_db_odds, update_db_odds, delete_from_odds

def hello_world():
    return response('Welcome to apiv1', 200)

def get_odds():
    data = get_db_odds()
    return response(data, 200)

def get_create():
    request_body = request.get_json()
    add_db_odds(request_body)
    return response("success! created ", 201)

def get_update(ids):
    request_body = request.get_json()
    update_db_odds(request_body, ids)
    return response("success!", 202)

def delete_odd(ids):
    delete_from_odds(ids)
    return response("success!", 202)