from flask import Flask, render_template, request
from manter.entities import Cliente
from manter.dao import DaoCliente
# importando a variavel app do __init__.py
from . import app
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cliente/add")
def cliente_add():
    return render_template('cadastro_cliente.html')

@app.route("/save", methods=["POST"])
def save():
    # recebe os campos do formulario
    # criar o objeto cliente
    # chamar a dao que salva no banco de dados
    nome = request.form.get("nome")
    cpf = request.form.get("cpf")
    email = request.form.get("email")
    cliente = Cliente(nome, cpf, email)
    dao = DaoCliente()
    dao.save(cliente)
    return findall()

@app.route("/delete/<id>")
def delete(id):
    # select from cliente where id = id
    # consulta o banco, e recupera o cliente
    # cliente = Database.getCliente(id)
    # Database.delete(cliente.id)
    return "manter.html"

@app.route("/update")
def update():
    # alem dos atributos eh necessario o ID
    # cliente = Database.find(id)
    # atualiza os campos...
    # Database.update(cliente)
    return "manter.html"

@app.route("/cliente/findall/")
def findall():
    dao = DaoCliente()
    clientes = dao.findall()
    return render_template("manter.html", clientes=clientes)
