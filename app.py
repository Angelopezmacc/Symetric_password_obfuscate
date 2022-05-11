from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import os

dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
db = SQLAlchemy(app)

# class Posts(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(50))
class Users(db.Model)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
