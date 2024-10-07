from flask import Blueprint, request, jsonify
from app.main.service.product_service import ProductService






product_routes = Blueprint('product_routes', __name__)

@product_routes.route('/products', methods=['GET'])
def get_products():
    products = ProductService.get_all_products()
    return jsonify([{'id': p.id, 'name': p.name, 'price': p.price, 'supplier_id': p.supplier_id} for p in products])

@product_routes.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_product = ProductService.add_product(data)
    return jsonify({'id': new_product.id}), 201

@product_routes.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    updated_product = ProductService.update_product(id, data)
    return jsonify({'id': updated_product.id})

@product_routes.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    ProductService.delete_product(id)
    return jsonify({'message': 'Product deleted'}), 204
