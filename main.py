from flask import Flask, render_template
from geradores import gerador_mega_sena

app = Flask(__name__)

@app.route("/")
def hello_world():
    numeros = gerador_mega_sena()
    return render_template("base.html", numeros=numeros)
