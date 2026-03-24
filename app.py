from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Sunscreen SPF 50", "brand": "Mother of Pearl", "price": 120000},
    {"id": 2, "name": "Moisturizer Ceramide", "brand": "Skintific", "price": 150000}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"status": "success", "data": products}), 200

@app.route('/products', methods=['POST'])
def add_product():
    new_item = request.json
    products.append(new_item)
    return jsonify({"status": "success", "message": "Produk berhasil ditambahkan"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)