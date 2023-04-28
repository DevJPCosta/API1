from flask import Flask, jsonify, request
from firebase_admin import credentials
from flask_firebase_admin import FirebaseAdmin


app = Flask(__name__)
app.config["FIREBASE_ADMIN_CREDENTIAL"] = credentials.Certificate(
    r"C:\Users\joao.santos\Documents\DEV\PythonApi\firebase.json")
app.config["FIREBASE_ADMIN_AUTHORIZATION_SCHEME"] = "JWT"
app.config["FIREBASE_ADMIN_CHECK_REVOKED"] = False
app.config["FIREBASE_ADMIN_PAYLOAD_ATTR"] = "firebase_jwt"
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


if __name__ == "__main__":
    app.run(debug=True)
