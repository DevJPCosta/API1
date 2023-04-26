from flask import Flask, render_template, request
import pyrebase


app = Flask(__name__)

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


@app.route('/get-data')
def get_data():
    data = db.child("example_node").get()
    return render_template('get_data.html', data=data.val())


if __name__ == '__main__':
    app.run(debug=True)
