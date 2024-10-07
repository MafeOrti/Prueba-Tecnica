from flask import request
from flask_restx import Resource

from app.main.service.inventory_service import (
    getAllProducts,
    getOneProduct,
    saveNewProduct,
    updateProduct,
    deleteProduct,
)
from ..dto.inventory_dto import InventoryDto

api = InventoryDto.api
product_dto = InventoryDto.product
product_supplier = InventoryDto.product_with_supplier


@api.route("/")
class Product(Resource):

    @api.doc("inventory get one product")
    def get(self):
        return {'message': 'Not Implemented'}, 501


@api.route("/get-all")
class Products(Resource):
    
    @api.doc("logout a user")
    @api.marshal_with(product_supplier)
    def get(self):
        return getAllProducts()

