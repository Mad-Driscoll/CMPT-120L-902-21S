from flask import Flask
app = Flask(__name__)

from flask import render_template

@app.route('/')
def index():
    return 'Index Page'

@app.route('/aboutme/')
def aboutme():
    return render_template('aboutme.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

@app.route('/resume/')
def resume():
    return render_template('resume.html')