
from flask import Flask, render_template
app = Flask(__name__, template_folder='templete')

@app.route('/')

def index():
    return render_template("index.html")
    # return ('Hello World!') 

@app.route('/racing')

def racing():
    return ("I will race this season!!")

@app.route("/baneshor")

def bane():
    return "walk"


if(__name__ == "__main__"):
    app.run(debug=True, port=8000)

    