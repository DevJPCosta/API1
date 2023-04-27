from flask import Flask, jsonify, request
from flask_firebase_admin import FirebaseAdmin

config = {
    "apiKey": "AIzaSyAQsgygjK06AsyrAKg_HrbvO4dzItFeYTU",
    "authDomain": "conecaooporapi.firebaseapp.com",
    "databaseURL": "https://conecaooporapi-default-rtdb.firebaseio.com",
    "projectId": "conecaooporapi",
    "storageBucket": "conecaooporapi.appspot.com",
    "messagingSenderId": "467005917293",
    "appId": "1:467005917293:web:1aa02d35bb9483ae8b976"
}

cred = firebase_admin.Credentials.from_service_account_file(
    r"C:\Users\joao.santos\Documents\DEV\PythonApi\firebase.json")

firebase = pyrebase.initialize_app(config)

firebase_admin.initialize_app(cred)

storage = firebase.storage()

app = Flask(__name__)
firebase = FirebaseAdmin(app)

livros = [
    {
        "id": 1,
        "titulo": "O Senhor dos Anéis - A Sociedade do Anel",
        "autor": "J.R.R Tolkien"
    },
    {
        "id": 2,
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": "J.K Howling"
    },
    {
        "id": 3,
        "titulo": "Hábitos Atômicos",
        "autor": "James Clear"
    },
]

# Consultar (todos)


@app.route("/livros", methods=["GET"])
def obter_livros():
    return jsonify(livros)

# Consultar (id)


@app.route("/livros/<int:id>", methods=["GET"])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)


# Editar
@app.route("/livros/<int:id>", methods=["PUT"])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])


# Criar
@app.route("/livros", methods=["POST"])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)


# Excluir
@app.route("/livros/<int:id>", methods=["DELETE"])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            del livros[indice]

    return jsonify(livros)


app.run(debug=True)
