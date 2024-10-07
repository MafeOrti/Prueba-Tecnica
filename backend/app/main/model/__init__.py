# app/main/__init__.py
from flask import Flask
from database import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Ajusta la URI de tu base de datos
    db.init_app(app)

    with app.app_context():
        from app.main.model.product import Product
        from app.main.model.supplier import Supplier

        # Crear las tablas si no existen
        db.create_all()

    return app
