from app.main.model.product import Product
from database import db

class ProductService:
    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def add_product(data):
        new_product = Product(name=data['name'], price=data['price'], supplier_id=data['supplier_id'])
        db.session.add(new_product)
        db.session.commit()
        return new_product

    @staticmethod
    def update_product(id, data):
        product = Product.query.get_or_404(id)
        product.name = data['name']
        product.price = data['price']
        product.supplier_id = data['supplier_id']
        db.session.commit()
        return product

    @staticmethod
    def delete_product(id):
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return product
