import os              

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta

from sequrity import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)

# use SQLite locally, if DB_URL is not defined
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')

# SQLAlchemy has already modif tracker
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# change the url: /login instead of /auth (by default)
app.config['JWT_AUTH_URL_RULE'] = '/login'

# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

# config JWT auth key name is 'email' instead of default 'username'
app.config['JWT_AUTH_USERNAME_KEY'] = 'email'
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
