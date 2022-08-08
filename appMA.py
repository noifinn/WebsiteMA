from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import psycopg2

appMA=Flask(__name__)
appMA.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:N01gym2,19@localhost/Benutzerdaten'
db=SQLAlchemy(appMA)



class BookData(db.Model):
    __tablename__ = "bookdata"
    id = db.Column(db.Integer, primary_key=True)
    autorin = db.Column(db.String(100))
    name = db.Column(db.String(100))
    preis = db.Column(db.Integer, nullable=False)
    zustand = db.Column(db.String(100))


    def __init__(self, autorin, name, preis, zustand):
        self.autorin_ = autorin
        self.name_ = name
        self.preis_ = preis
        self.zustand_ = zustand

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_= db.Column(db.String(100), unique=True)
    password_= db.Column(db.String(100))
    username_ = db.Column(db.String(30), unique=True)


    def __init__(self, email_, password_, username_):
        self.email_ = email_
        self.password_ = password_
        self.username_ = username_

@appMA.route("/", methods=["POST", "GET"])                          #Passwort und Email werden gelesen, falls man über "Login" auf die Homepage kommt
def homepage():
    if request.method == "POST":
        email = request.form["email_name"]
        password = request.form["password_name"]
        username = request.form["user_name"]
        print(email, password, username)
        data = Data(email, password, username)
        db.session.add(data)
        db.session.commit()
    return render_template("homepage.html", methods=["POST", "GET"])

@appMA.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email_name"]
        password = request.form["password_name"]
        username = request.form["user_name"]
        print(email, password, username)
        data = Data('rrr', 'rrr', 'rrr')
        db.session.add(data)
        print(data, 'after')
        db.session.commit()

    return render_template("login.html", methods=["POST", "GET"])

@appMA.route("/registrieren", methods=["POST", "GET"])
def registrieren():
    return render_template("registrieren.html", methods=["POST", "GET"])

@appMA.route("/upload", methods=["POST", "GET"])
def upload():
    return render_template("upload.html", methods=["POST", "GET"])

@appMA.route("/results", methods=["POST", "GET"])
def results():
        if request.method == "POST":
            autorin = request.form["autorin_name"]
            name = request.form["book_name"]
            preis = request.form["preis_name"]
            zustand = request.form["zustand_name"]
            print(autorin, name, preis, zustand)
            """bookdata = BookData(autorin, name, preis, zustand)"""
            bookdata = BookData('hhh','jjj' , 'iiii', 'ooo')
            print(bookdata, 'before')
            db.session.add(bookdata)
            print(bookdata, 'after')
            db.session.commit()
        return render_template("results.html", methods=["POST", "GET"])

@appMA.route("/meinkonto", methods=["POST", "GET"])
def meinkonto():
    pass

if __name__ == '__main__':
    appMA.debug=True
    appMA.run()
