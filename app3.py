from flask import Flask, jsonify
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

app = Flask(__name__)


@app.route('/data')
def get_data():
    db = firebase.database()
    data = db.child("users").get().val()
    return jsonify(data)


if __name__ == '__main__':
    app.run()
