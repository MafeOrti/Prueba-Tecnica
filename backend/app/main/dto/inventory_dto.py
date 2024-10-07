from flask_restx import Namespace, fields
from sqlalchemy import Integer


class InventoryDto:
    api = Namespace('inventory', description='inventory related operations')
    
    product_with_supplier = api.model('product_supplier', {
        'id_product': fields.Integer(required=True, description='prodict id'),
        'name': fields.String(required=True, description='product name'),
        'quantity': fields.String(required=True, description='quantity product'),
        'price_unit': fields.String(required=True, description='product price'),
        'id_supplier': fields.Integer(required=True, description='prodict supplier id'),
        'supplier': fields.String(required=True, description='supplier name')
    })
    
    product = api.model('product', {
        'id_product': fields.Integer(required=True, description='prodict id'),
        'name': fields.String(required=True, description='product name'),
        'quantity': fields.String(required=True, description='quantity product'),
        'price_unit': fields.String(required=True, description='product price'),
    })
