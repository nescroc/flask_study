from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome'

@app.route('/create/')
def create():
    return "Create"

@app.route('/read/1')
def create():
    return "Read 1"


app.run(port=8080,debug=True)