import os
import sys
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

WIN = sys.platform.startswith('win')
if WIN:
	prefix = 'sqlite:///'
else:
	prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db =  SQLAlchemy(app)


name = 'navy Song'
movies = [
	{'title':'肖申克的救赎The Shawshank Redemption', 'year': '1994'},
	{'title':'控方证人witness for the Prosecution', 'year': '1957'},
	{'title':'这个杀手不太冷', 'year': '1994'},
	{'title':'霸王别姬', 'year': '1993'},
	{'title':'美丽人生', 'year': '1997'},
	{'title':'阿甘正传Forrest Gump', 'year': '1994'},
	{'title':'辛德勒的名单Schindler\'s List', 'year': '1993'},
	{'title':'教父The Godfather', 'year': '1972'},
	]


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(20))


class Movie(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(60))
	year = db.Column(db.String(4))
	
@app.context_processor
def inject_user():
	user = User.query.first()
	return dict(user=user)

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():	
	movies = Movie.query.all()
	return render_template('index.html', movies=movies)
	

