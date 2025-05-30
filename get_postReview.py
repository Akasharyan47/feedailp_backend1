from flask import Flask, jsonify, request
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
import os

app = Flask(__name__)

# Secure CORS - Allow only your frontend domain during deployment
CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

# Initialize Firebase Admin SDK only once
if not firebase_admin._apps:
    cred = credentials.Certificate('./feedailp-login-firebase-adminsdk-y6v1o-49cd95f4b5.json')
    firebase_admin.initialize_app(cred)

db = firestore.client()

# ✅ Get All Service Types
@app.route('/api/service-types', methods=['GET'])
def get_service_types():
    try:
        docs = db.collection('service_types').stream()
        service_types = [
            {
                "service_type_id": doc.to_dict().get("service_type_id"),
                "service_type_nm": doc.to_dict().get("service_type_nm")
            } for doc in docs
        ]
        return jsonify({"status": "success", "data": service_types}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ✅ Get Brands by Service Type ID
@app.route('/api/brands/<string:service_type_id>', methods=['GET'])
def get_brands_by_service_type(service_type_id):
    try:
        docs = db.collection('brands').where('service_type_id', '==', service_type_id).stream()
        brands = [
            {
                "brand_id": doc.to_dict().get("brand_id"),
                "brand_name": doc.to_dict().get("brand_name")
            } for doc in docs
        ]
        return jsonify({"status": "success", "data": brands}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ✅ Get Products by Brand ID
@app.route('/api/products/<string:brand_id>', methods=['GET'])
def get_products_by_brand(brand_id):
    try:
        docs = db.collection('products').where('brand_id', '==', brand_id).stream()
        products = [
            {
                "product_id": doc.to_dict().get("product_id"),
                "product_nm": doc.to_dict().get("product_nm")
            } for doc in docs
        ]
        return jsonify({"status": "success", "data": products}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Optional Health Check
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "API is running"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
