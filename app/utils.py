from flask import make_response, jsonify

def response(data, status):
    return make_response(jsonify({
        'data': data
        })), status
