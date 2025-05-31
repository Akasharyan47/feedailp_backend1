from flask import Flask, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("firebaseConfig.json")  # Make sure this file is uploaded
firebase_admin.initialize_app(cred)
db = firestore.client()

# Route to get all service types
@app.route("/service_types", methods=["GET"])
def get_service_types():
    service_types = [doc.to_dict() for doc in db.collection("service_types").stream()]
    return jsonify(service_types)

# Route to get brands by service_type_id
@app.route("/brands/<service_type_id>", methods=["GET"])
def get_brands(service_type_id):
    brands = db.collection("brands").where("service_type_id", "==", service_type_id).stream()
    return jsonify([doc.to_dict() for doc in brands])

# Route to get products by brand_id
@app.route("/products/<brand_id>", methods=["GET"])
def get_products(brand_id):
    products = db.collection("products").where("brand_id", "==", brand_id).stream()
    return jsonify([doc.to_dict() for doc in products])

# Run app locally (ignored in Render but useful for local dev)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
