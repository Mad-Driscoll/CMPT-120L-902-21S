from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/')
def index():
    return render_template('index.html')