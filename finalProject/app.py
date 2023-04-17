import os
from datetime import datetime

from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.debug = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Session(app)

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    email = db.Column("email", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email




@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/")
def index():
    return render_template("index.html", image=url_for('static', filename='logo.png'))

@app.route("/gallery")
def gallary():
    return render_template("gallery.html")

@app.route("/classInfo", methods=["GET", "POST"])
def classInfo():
    # if request.method == "POST":
    return render_template("class.html")

@app.route("/apply", methods=["GET", "POST"])
def apply():
    return render_template("apply.html")
    
    

    
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)