from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///to_do.db"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db= SQLAlchemy(app)
# db.Model.metadata.reflect(db.engine)


class To_do(db.Model):
  sno=db.Column(db.Integer, primary_key=True)
  title= db.Column(db.String(200), nullable=False)
  description=db.Column(db.String(400), nullable=False)
  date_created=db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return (self.sno)

# with app.app_context():
#   db.create_all()
    
@app.route('/')
def index_page():
  todo=To_do(title="HEllo", description= "Whatsupp I am Alex from Microsoft!!")
  db.session.add(todo)
  db.session.commit()
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