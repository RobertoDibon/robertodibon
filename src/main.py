from flask import Flask, render_template, redirect, url_for, flash

app = Flask(__name__)


# Rutas
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')




