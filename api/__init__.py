from flask import Flask, Blueprint

app = Flask(__name__)

## Initialize Config
app.config.from_pyfile("config.py")

## Config packages
from api.extensions import database
from api.extensions import jwt

## Blueprints
api = Blueprint('api', __name__)

from api.controllers import login_controller
from api.controllers import user_controller
from api.controllers import profile_controller

app.register_blueprint(api, url_prefix="/api")