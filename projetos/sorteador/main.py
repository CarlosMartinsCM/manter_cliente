from flask import Flask, render_template

app = Flask(__name__)

# cria uma rota para: http://127.0.0.1:5000/index
@app.route("/index")
def index():
    return render_template('index.html')
    # return "<h1>Olá, tudo certo por aqui!</h1>"

@app.route("/gerar")
def gerar():
    # eh o onde a magica acontece...
    # gerar os numeros
    # e retorna os numero para a view (index.html)
    from random import randrange

    numeros = [11, 22, 33, 44, 55, 60]
    # executa 6 vezes de 0 a 5
    for c in range(0, 6):
        # rand gera os numero aleatoriamente (1 a 60)
        numeros[c] = randrange(1, 60)

    return render_template('index.html', numeros=numeros)

# outra rota: http://127.0.0.1:5000/logout
@app.route("/logout")
def logout():
    return "<h1>Adios!</h1>"

# MUITO, MAS MUITO IMPORTANTE!!!! ATIVAR O DEGUB
app.run(debug=True)
