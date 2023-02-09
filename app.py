from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templete')

app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///to_do.db"

db= SQLAlchemy(app)

@app.route('/')

def index_page():
    return render_template("index.html")
    # return ('Hello World!') 

@app.route('/racing')

def racing_car():
    return ("I will race this season!!")

@app.route("/baneshor")

def bane_to_college():
    return "walk"


if(__name__ == "__main__"):
    app.run(debug=True, port=8000)

    