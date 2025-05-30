import firebase_admin
from firebase_admin import credentials, firestore, initialize_app  # 👈 Yeh line zaroori hai
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('./feedailp-login-firebase-adminsdk-y6v1o-49cd95f4b5.json')
initialize_app(cred)
db = firestore.client()

# Step 1: Add service_types
service_types = [
    {"service_type_id": "electronics_repair", "service_type_nm": "Repair"},
    {"service_type_id": "experience_review", "service_type_nm": "Experience Review"},
]

for service in service_types:
    doc_ref = db.collection('service_types').document(service['service_type_id'])
    doc_ref.set(service)

# Step 2: Add brands (for experience_review)
brands = [
    {"brand_id": "apple", "brand_name": "Apple", "service_type_id": "experience_review"},
    {"brand_id": "samsung", "brand_name": "Samsung", "service_type_id": "experience_review"},
    {"brand_id": "dell", "brand_name": "Dell", "service_type_id": "experience_review"},
    {"brand_id": "hp", "brand_name": "HP", "service_type_id": "experience_review"},
    {"brand_id": "xiaomi", "brand_name": "Xiaomi", "service_type_id": "experience_review"},
    {"brand_id": "lenovo", "brand_name": "Lenovo", "service_type_id": "experience_review"},
]

for brand in brands:
    doc_ref = db.collection('brands').document(brand['brand_id'])
    doc_ref.set(brand)

# Step 3: Add products
products = [
    {"product_id": "iphone_15", "product_nm": "iPhone 15", "service_type_id": "experience_review", "brand_id": "apple"},
    {"product_id": "macbook_air", "product_nm": "MacBook Air", "service_type_id": "experience_review", "brand_id": "apple"},
    {"product_id": "galaxy_s23", "product_nm": "Galaxy S23", "service_type_id": "experience_review", "brand_id": "samsung"},
    {"product_id": "galaxy_tab", "product_nm": "Galaxy Tab", "service_type_id": "experience_review", "brand_id": "samsung"},
    {"product_id": "dell_xps", "product_nm": "Dell XPS", "service_type_id": "experience_review", "brand_id": "dell"},
    {"product_id": "hp_pavilion", "product_nm": "HP Pavilion", "service_type_id": "experience_review", "brand_id": "hp"},
    {"product_id": "redmi_note", "product_nm": "Redmi Note", "service_type_id": "experience_review", "brand_id": "xiaomi"},
    {"product_id": "lenovo_thinkpad", "product_nm": "Lenovo ThinkPad", "service_type_id": "experience_review", "brand_id": "lenovo"},
]

for product in products:
    doc_ref = db.collection('products').document(product['product_id'])
    doc_ref.set(product)

brand_questions = [
    {
        "brand_id": "apple",
        "rating_questions": [
            "Hate your overall service experience with the company?",
            "Rate the professionalism and friendliness of the service representative during service contact?",
            "Rate the knowledge and skills of the service representative?",
            "Rate the quality of the service?"
        ],
        "yes_no_questions": [
            "Was the pricing of the service reasonable and fair?",
            "Was the price charged more than the actual amount?",
            "Was your issue resolved within the time frame?",
            "Were you informed about any additional charges or fees before the service was provided?"
        ]
    },
    {
        "brand_id": "samsung",
        "rating_questions": [
            "How satisfied are you with Samsung's after-sales support?",
            "Rate the timeliness of Samsung’s service response.",
            "Rate the expertise of the Samsung service staff.",
            "Rate the overall product performance."
        ],
        "yes_no_questions": [
            "Was the service pricing reasonable?",
            "Did Samsung explain the charges clearly?",
            "Was your Samsung issue fixed on time?",
            "Were you kept informed about the repair process?"
        ]
    },
    # Add other brands similarly...
]

for bq in brand_questions:
    doc_ref = db.collection('brand_questions').document(bq['brand_id'])
    doc_ref.set(bq)

print("✅ Brand questions uploaded successfully.")


print("✅ Data upload successful.")
