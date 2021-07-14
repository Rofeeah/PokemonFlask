# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
# from flask import request


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    props = {
        'name': 'Blazikan',
        'start-as': 'Torchic',
        'type': 'fire'
    }
    return render_template('index.html', props = props)

@app.route('/secret')
def secret():
    return "yo wasssupp"

@app.route('/resultspage')
def resultspage():
    dessert = {
        'dessert': 'pie'
    }
    return render_template('resultspage.html', foods = dessert)

