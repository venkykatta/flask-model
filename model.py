from flask import Flask
from flask_mysqldb import MySQL
from flask_mysqldb import db


app = Flask(__name__)

@app.route('/')
def index():
    return "A"

class user(db.Model):
    id = db.Column(db.integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)


if __name__ == "__main__":
    app.run(debug=True)
