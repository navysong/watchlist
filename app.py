from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():	
	return render_template('index.html', name=name, movies=movies)
	
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