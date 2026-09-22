from .db import migrate,db
from .config import Config 
from flask import Flask 
from .routes import *
from flask_restful import Api
from .models import *

def create_app():
    app=Flask(__name__)
    
    app.config.from_object(Config)
    app.json.compact=False

    migrate.init_app(app,db)
    db.init_app(app)
    api=Api(app)

    api.add_resource(Home,"/")

    return app