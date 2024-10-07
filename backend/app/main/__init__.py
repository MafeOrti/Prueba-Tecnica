from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_migrate import Migrate
from .config import config_by_name
from .constants import ORIGINS
import os
import jinja2


db = SQLAlchemy()
flask_bcrypt = Bcrypt()

migrate = Migrate()


def create_app(config_name):
    cwd = os.getcwd()
    template_dir = os.path.abspath('../../templates')
    static_dir = os.path.abspath('../../templates/dist/static')
    app = Flask(__name__, static_folder='../../templates/dist/static' , template_folder='../template')
    app.jinja_loader = jinja2.FileSystemLoader('../files/templates')
    app.config.from_object(config_by_name[config_name])
    
    CORS(app, origins= ORIGINS, supports_credentials=True, expose_headers= 'Content-Disposition')

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization, Content-Disposition')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response
    
    
    db.init_app(app)
    flask_bcrypt.init_app(app)
    migrate.init_app(app, db)
    return app