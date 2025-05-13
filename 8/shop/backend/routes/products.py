from flask import Blueprint, jsonify, session

products_bp = Blueprint('products', __name__, url_prefix='/products')
@products_bp.route('/', methods=['GET'])

def get_products():
    if 'user_id' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    products = [
        {"id": 1, "name": "Product 1", "price": 10.0},
        {"id": 2, "name": "Product 2", "price": 20.0},
        {"id": 3, "name": "Product 3", "price": 30.0},
    ]
    return jsonify(products), 200