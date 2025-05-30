@app.route("/service_types", methods=["GET"])
def get_service_types():
    service_types = [doc.to_dict() for doc in db.collection("service_types").stream()]
    return jsonify(service_types)

@app.route("/brands/<service_type_id>", methods=["GET"])
def get_brands(service_type_id):
    brands = db.collection("brands").where("service_type_id", "==", service_type_id).stream()
    return jsonify([doc.to_dict() for doc in brands])

@app.route("/products/<brand_id>", methods=["GET"])
def get_products(brand_id):
    products = db.collection("products").where("brand_id", "==", brand_id).stream()
    return jsonify([doc.to_dict() for doc in products])
