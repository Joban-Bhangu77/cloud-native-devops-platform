from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory product list
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Phone", "price": 500},
]

# Home Route (Beautiful UI)
@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>🚀 Joban's Cloud-Native App</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                color: white;
                text-align: center;
                padding-top: 80px;
                margin: 0;
            }
            h1 {
                font-size: 48px;
                margin-bottom: 10px;
            }
            p {
                font-size: 20px;
                margin: 8px 0;
            }
            .box {
                background: rgba(255,255,255,0.1);
                padding: 40px;
                border-radius: 20px;
                display: inline-block;
                box-shadow: 0 0 25px rgba(0,0,0,0.6);
            }
            .highlight {
                color: #00ffd5;
                font-weight: bold;
            }
            code {
                background: rgba(0,0,0,0.3);
                padding: 5px 10px;
                border-radius: 8px;
            }
            .footer {
                margin-top: 20px;
                font-size: 16px;
                opacity: 0.8;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1>🚀 Welcome to Joban’s Cloud-Native App 🌍</h1>
            
            <p>🔥 Deployed on <span class="highlight">AWS EKS</span> using Kubernetes</p>
            <p>⚡ Powered by <span class="highlight">Docker + Flask + DevOps</span></p>
            <p>☁️ Running on <span class="highlight">Fargate + EC2 Hybrid Architecture</span></p>
            <p>🔐 Built with scalable & secure cloud infrastructure</p>
            
            <br>
            
            <p>📦 Microservices Ready | 🚀 Production Grade | 🌐 Cloud Native</p>
            
            <br>
            
            <p>👉 Test API: <code>/products</code></p>
            <p>👉 Add Product: POST to <code>/products</code></p>
            
            <br>
            
            <p>👨‍💻 Built by <span class="highlight">Jobanjit Singh</span></p>
            <p class="footer">💡 Next: CI/CD • Terraform • AI Automation 🚀</p>
            
            <br>
            
            <p>✨ Keep Building. Keep Scaling. Keep Winning. 💯</p>
        </div>
    </body>
    </html>
    """, 200


# GET Products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200


# ADD Product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()

    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_id = max(p["id"] for p in products) + 1
    new_product = {
        "id": new_id,
        "name": data["name"],
        "price": data["price"]
    }

    products.append(new_product)

    return jsonify(new_product), 201


# Run App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)