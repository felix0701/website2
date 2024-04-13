import firebase_admin
from firebase_admin import credentials

# Initialize the Firebase Admin SDK
cred = credentials.Certificate("path/to/your/firebase-credentials.json")
firebase_admin.initialize_app(cred)
