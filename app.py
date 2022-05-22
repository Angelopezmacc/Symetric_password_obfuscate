from flask import Flask,render_template,url_for,redirect,flash,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request
from Crypto.Cipher import AES
import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True , nullable=False)
    password = db.Column(db.String(80), nullable = False)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():
    pass

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        hashed_pw = generate_password_hash(request.form["password"], method="sha256")
        new_user = Users(username=request.form["username"], password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("signup.html")

@app.route("/login")
def login():
    if request.method == "POST":
        user = Users.query.filter_by(username=request.form["username"]).first()

        if user and check_password_hash(user.password,request.form["password"]):
            data = request.json
            return jsonify(data)
            # usuario = request.form.get("username")
            # return redirect(url_for("foo"))
        # return request.form



    #     return " Usuario o contraseña incorrectos"

    return render_template("login.html")

@app.route('/foo', methods=['POST']) 
def foo():
    data = request.json
    return jsonify(data)     


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
