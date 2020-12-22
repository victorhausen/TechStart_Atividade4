from flask import Flask, render_template
from controller import Controller

import view
app = Flask(__name__)

@app.route("/")
def index():
    return("""
    <h2><a href='/read_marketplaces'>Lista de Market Places</a></h2>
    <h2><a href='/read_categories'>Lista de Categorias</a></h2>
    """)

@app.route("/read_marketplaces")
def read_marketplaces():

    content = Controller.read_marketplaces()
    return render_template("read_marketplaces.html", table=content)


#@app.route("read_categories")

app.run(debug = True)