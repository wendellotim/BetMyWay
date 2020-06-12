from flask import Flask

from flask import request

app = Flask(__name__)


@app.route('/getjson', methods = ['GET'])
def getJsonHandler():
    print (request.is_json)
    content = request.get_json("https://reqres.in/api/users")
    print(content)
    return content
    
