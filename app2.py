import pyrebase
import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

config = {
    "apiKey": "AIzaSyAQsgygjK06AsyrAKg_HrbvO4dzItFeYTU",
    "authDomain": "conecaooporapi.firebaseapp.com",
    "databaseURL": "https://conecaooporapi-default-rtdb.firebaseio.com",
    "projectId": "conecaooporapi",
    "storageBucket": "conecaooporapi.appspot.com",
    "messagingSenderId": "467005917293",
    "appId": "1:467005917293:web:1aa02d35bb9483ae8b976"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

# storage.child("images/new.jpg").put("img.jpg")

storage.child("images/new.jpg").download("example.jpg")

print(storage.child("images/new.jpg").get_url(None))
