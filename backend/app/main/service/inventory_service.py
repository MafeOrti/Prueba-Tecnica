import datetime
import logging
from app.main import db
from ..model.product import Product
from ..model.supplier import Supplier


def getAllProducts():
    try:
        response = (
            db.session.query(
                Product.id_product,
                Product.name,
                Product.price_unit,
                Product.quantity,
                Supplier.id_supplier,
                Supplier.name,
            )
            .join(Supplier, Supplier.id_supplier == Product.id_supplier, isouter=True)
            .all()
        )
        keys_response = [
            'id_product',
            'name',
            'price_unit',
            'quantity',
            'id_supplier',
            'supplier'
        ]
        return [ dict(zip(keys_response, item)) for item in response ]
    except Exception as e:
        logging.error(e)
        response = {"message": "Error: " + str(e)}
        return response, 500
    finally:
        db.session.close()


def getOneProduct(id):
    try:
        response = Product.query.filter(Product.id_product == id).first()
        return response
    except Exception as e:
        logging.error(e)
        response = {"message": "Error: " + str(e)}
        return response, 500
    finally:
        db.session.close()


def saveNewProduct(product):
    return {'message': 'Not Implemented'}, 501


def updateProduct(product):
    return {'message': 'Not Implemented'}, 501


def deleteProduct(id):
    return {'message': 'Not Implemented'}, 501
