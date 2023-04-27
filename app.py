from flask import Flask, request
from firebase_admin import credentials
from flask_firebase_admin import FirebaseAdmin

app = Flask(__name__)
app.config["FIREBASE_ADMIN_CREDENTIAL"] = credentials.Certificate(
    r"C:\Users\joao.santos\Documents\DEV\PythonApi\firebase.json")
app.config["FIREBASE_ADMIN_AUTHORIZATION_SCHEME"] = "JWT"
app.config["FIREBASE_ADMIN_CHECK_REVOKED"] = False
app.config["FIREBASE_ADMIN_PAYLOAD_ATTR"] = "firebase_jwt"


firebase = FirebaseAdmin(app)


@app.route("/unprotected")
def unprotected():
    return {"message": "Hello anonymous user!"}


@app.route("/protected")
@firebase.jwt_required
def protected():
    return {"message": f"Hello {request.jwt_payload['email']}!"}


if __name__ == "__main__":
    app.run(debug=True)
