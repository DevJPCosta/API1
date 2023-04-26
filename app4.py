import pyrebase

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
auth = firebase.auth()
user = auth.sign_in_with_email_and_password("jpcsnt0s@gmail.com", "COBRAl&ao7")
db = firebase.database()


@app.route('/')
def hello_world():
    return 'Hello, World!'
