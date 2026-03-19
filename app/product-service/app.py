from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 500},
]

@app.route('/')
def home():
    return "Flask App Running 🚀", 200

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    new_id = max(p["id"] for p in products) + 1
    data["id"] = new_id
    products.append(data)

    return jsonify(data), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)