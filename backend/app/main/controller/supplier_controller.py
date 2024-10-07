from flask import Blueprint, request, jsonify
from app.main.service.supplier_service import SupplierService

supplier_routes = Blueprint('supplier_routes', __name__)

@supplier_routes.route('/suppliers', methods=['GET'])
def get_suppliers():
    suppliers = SupplierService.get_all_suppliers()
    return jsonify([{'id': s.id, 'name': s.name} for s in suppliers])

@supplier_routes.route('/suppliers', methods=['POST'])
def add_supplier():
    data = request.get_json()
    new_supplier = SupplierService.add_supplier(data)
    return jsonify({'id': new_supplier.id}), 201

@supplier_routes.route('/suppliers/<int:id>', methods=['PUT'])
def update_supplier(id):
    data = request.get_json()
    updated_supplier = SupplierService.update_supplier(id, data)
    return jsonify({'id': updated_supplier.id})

@supplier_routes.route('/suppliers/<int:id>', methods=['DELETE'])
def delete_supplier(id):
    SupplierService.delete_supplier(id)
    return jsonify({'message': 'Supplier deleted'}), 204
