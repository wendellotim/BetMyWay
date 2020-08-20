from flask import Flask
from app.welcome import hello_world, get_odds, get_create, get_update, delete_odd
from .db_setup import create_odds_table

app = Flask(__name__)

create_odds_table()

# Add url rules endpoints
app.add_url_rule('/api/v1/', view_func=hello_world, methods=['GET'])
app.add_url_rule('/', view_func=hello_world, methods=['GET'])
app.add_url_rule('/api/v1/odds/read/', view_func=get_odds, methods=['GET'])
app.add_url_rule( '/api/v1/odds/create/', view_func=get_create, methods=['POST'])
app.add_url_rule( '/api/v1/odds/update/<int:ids>', view_func=get_update, methods=['PUT'])
app.add_url_rule( '/api/v1/odds/delete/<int:ids>', view_func=delete_odd, methods=['DELETE'])


