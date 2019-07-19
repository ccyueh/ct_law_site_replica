from app import app
from flask import render_template, url_for

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/who')
def who():
    return render_template('who.html')

@app.route('/what')
def what():
    return render_template('what.html')

@app.route('/where')
def where():
    return render_template('where.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
