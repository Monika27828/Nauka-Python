from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/api/products', methods=['GET'])
def get_products():
    products = Product.guery.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price} for p in products])

@app.route('/api/products', methods=['POST'])
def add_product():
    data = request.get_json()
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Invalid data"}), 400

    new_product = Product(name=data["name"], price=float(data["price"]))
    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product added!"}), 201

@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted"}), 200

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)