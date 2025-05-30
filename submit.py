import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK (sirf ek baar chalana hai)
cred = credentials.Certificate('./feedailp-login-firebase-adminsdk-y6v1o-49cd95f4b5.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def save_user_submission(data):
    """
    Firestore me user submission ko 'user_submissions' collection me save karta hai.
    data: dict (structured data)
    """
    try:
        doc_ref = db.collection('user_submissions').document()  # auto-generated ID
        data['timestamp'] = firestore.SERVER_TIMESTAMP  # Firestore server timestamp
        doc_ref.set(data)
        print("✅ Submission saved successfully.")
    except Exception as e:
        print("❌ Error saving submission:", e)

if __name__ == "__main__":
    # Sample data for testing
    user_data = {
        "service_type": "electronics_repair",
        "brand": "Apple",
        "product": "iPhone 15",
        "feedback_text": "Screen replaced successfully",
        "ratings": {
            "professionalism": 5,
            "quality": 4
        },
        "pricing_reasonable": True,
        "price_charged_extra": False,
        "issue_resolved": True,
        "additional_charges": False
    }

    save_user_submission(user_data)
