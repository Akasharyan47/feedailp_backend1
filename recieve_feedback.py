from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # ye sab origins ke liye allow kar dega OPTIONS requests ko

@app.route('/api/save-feedback', methods=['POST', 'OPTIONS'])
def save_feedback():
    if request.method == 'OPTIONS':
        # CORS preflight request ke liye 200 response dena zaroori hai
        return '', 200
    data = request.json
    # aapka firebase save code yahan likho
    return jsonify({"status": "success"})
