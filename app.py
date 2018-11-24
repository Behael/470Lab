from flask import Flask, render_template, Markup, request, redirect, session, abort
import random

MyApp = Flask(__name__)

MyApp.secret_key = "mO0m0Of@rm!"

@MyApp.route("/")
def hello():
	return render_template('home.html')

@MyApp.route("/magic")
def magic():
	return render_template('magic.html')
 
@MyApp.route("/manga")
def manga():
	return render_template('manga.html')
 
@MyApp.route("/games")
def games():
	return render_template('games.html')

@MyApp.route("/470")
def cosc():
	if(session['login']):
	  return render_template('cosc.html')
	else:
	  abort(418)

@MyApp.route("/login")
def login():
	return render_template('login.html')

@MyApp.route("/logger", methods=['POST'])
def logger():
        username = request.form['uname']
	password = request.form['psw']

	if username == 'moo' and password == 'cow':
                session['login'] = 'The Cow King'
                return redirect("/")
        else:
                return redirect("/login")

@MyApp.route("/logout")
def logout():
	session.pop('login', None)
	return render_template('home.html')

@MyApp.errorhandler(418)
def test(e):
	return render_template('418.html'), 404

if __name__ == "__main__":
        MyApp.run()
