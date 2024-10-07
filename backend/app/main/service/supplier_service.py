from app.main.model.supplier import Supplier
from database import db

class SupplierService:
    @staticmethod
    def get_all_suppliers():
        return Supplier.query.all()

    @staticmethod
    def add_supplier(data):
        new_supplier = Supplier(name=data['name'])
        db.session.add(new_supplier)
        db.session.commit()
        return new_supplier

    @staticmethod
    def update_supplier(id, data):
        supplier = Supplier.query.get_or_404(id)
        supplier.name = data['name']
        db.session.commit()
        return supplier

    @staticmethod
    def delete_supplier(id):
        supplier = Supplier.query.get_or_404(id)
        db.session.delete(supplier)
        db.session.commit()
        return supplier
