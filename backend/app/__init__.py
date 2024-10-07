from flask_restx import Api
from flask import Blueprint
from flask import render_template, request
# backend/app/__init__.py
from flask import Flask
from backend.database import db  # Importa db desde el archivo correcto

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Ajusta la URI de tu base de datos
    db.init_app(app)

    with app.app_context():
        from app.main.model.product import Product
        from app.main.model.supplier import Supplier

        # Crea las tablas si no existen
        db.create_all()

    return app



import os

from .main.controller.inventory_controller import api as inventory_ns

blueprint = Blueprint('api', __name__, static_folder='../templates/dist/static' , template_folder='../template')

api = Api(blueprint,
          title='API',
          version='1.0',
          description='flask restplus web service'
          )

api.add_namespace(inventory_ns, path='/inventory')

@blueprint.route('/')
def home():
    return render_template('dist/index.html')
