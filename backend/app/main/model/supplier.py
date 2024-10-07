from .. import db

class Supplier(db.Model):
    __tablename__ = 'supplier'

    id_supplier = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, nullable=False)

    