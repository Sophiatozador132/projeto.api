from flask import Blueprint, app, jsonify
bp = Blueprint("api", __name__)

#Daqui pra baixo as rotas

@bp.route("/", methods=("GET",))
def index():
    return jsonify({"status": 200, "message": "API da Sophia Tozador"})
    
@bp.route("/aleatorios", methods=("GET",))
def aleatorios():
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@bp.route("/argumentos/<string:nome>")
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome})

@bp.route("/argumentos", methods=("GET",))
def arg_implicito():
    return jsonify({"status": 200, "data": Request.args["nome"]})

@bp.route("/idades", methods=("GET",))
def idades():
    from random_data import pessoas
    import funcoes
    num = funcoes.maior_de_50(pessoas)
    return jsonify({"status": 200, "data": num})

@bp.route("/salarios", methods=("GET",))
def salarios():
    from random_data import pessoas
    import funcoes
    num = funcoes.mais_2000(pessoas)
    return jsonify({"status": 200, "data": num})

if __name__ == '__main__':
    app.run(debug=True)