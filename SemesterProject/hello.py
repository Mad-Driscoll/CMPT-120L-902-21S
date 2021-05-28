from flask import Flask
from flask import logging
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    app.logger.info("Flying to the Index Page")
    return render_template('home.html')


@app.route('/aboutme/')
def aboutme():
    app.logger.info("Flying to the About Me Page")
    return render_template('aboutme.html')

@app.route('/gallery/')
def gallery():
    app.logger.info("Flying to the Gallery Page")
    return render_template('gallery.html')

@app.route('/home/')
def home():
    app.logger.info("Flying to the Home Page")
    return render_template('home.html')

@app.route('/contact/')
def contact():
    app.logger.info("Flying to the Contact Page")
    return render_template('contact.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.info("404: Page Not Found")
    return render_template('404.html'), 404