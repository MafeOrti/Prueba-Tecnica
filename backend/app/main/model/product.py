
from database import db
from .supplier import Supplier

# app/main/model/product.py
from database import db

class Product(db.Model):
    __tablename__ = 'product'

    id_product = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price_unit = db.Column(db.Numeric, nullable=False)
    id_supplier = db.Column(db.Integer, db.ForeignKey('supplier.id_supplier'), nullable=False)

    # Referenciar 'Supplier' como una cadena para evitar problemas de inicialización
    supplier = db.relationship('Supplier', backref='products')
