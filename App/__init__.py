from flask import Flask
from App.ext import init_ext
from App.settings import envs
from App.apis import init_apis
from flask_cors import *

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)
    app.config.from_object(envs.get("develop"))

    init_apis(app)
    init_ext(app)

    return app