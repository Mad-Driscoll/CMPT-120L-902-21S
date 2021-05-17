from flask import Flask
from flask import render_template
from flask import request
import logging

app = Flask(__name__)

@app.route('/')
def index():
    app.logger.info("Index Page")
    return ('Index Page')


@app.route('/aboutme/')
def aboutme():
    app.logger.info("About Me Page")
    return render_template('aboutme.html')

@app.route('/gallery/')
def gallery():
    app.logger.info("Gallery Page")
    return render_template('gallery.html')

@app.route('/resume/')
def resume():
    app.logger.info("Resume Page")
    return render_template('resume.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.info("404: Page Not Found")
    return render_template('404.html'), 404