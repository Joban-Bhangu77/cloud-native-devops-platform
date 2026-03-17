from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 500},
    {"id": 3, "name": "Tablet", "price": 300},
]

# API: Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

# API: Get product by id
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

# API: Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    new_id = max(p["id"] for p in products) + 1
    data["id"] = new_id
    products.append(data)
    return jsonify(data), 201

if __name__ == "__main__":
    # Listen on all interfaces so Docker can forward the port
    app.run(host="0.0.0.0", port=5000, debug=True)