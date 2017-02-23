from flask import Flask, render_template, jsonify, request
import sqlite3 as lite

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/movie', methods=['POST'])
def add_movie():
	con = lite.connect('database.db')
	curs = con.cursor()
	title = request.form['title']
	genre = request.form['genre']

	try:
		curs.execute('INSERT INTO movies(title, genre) VALUES(?,?)', (title, genre))
		con.commit()
		message = 'That\'s a great movie!'
	except:
		con.rollback()
		message = 'insertion error ;)'
	finally:
		con.close()
		return message

@app.route('/movies')
def movie_list():
	con = lite.connect('database.db')
	curs = con.cursor()

	curs.execute('SELECT * FROM movies')
	my_list = curs.fetchall()
	con.close()
	return jsonify(my_list)

app.run(debug = True)