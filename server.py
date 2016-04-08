# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("home.html")
	
@app.route("/about")
def about():
	return render_template("about.html")
	
@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/art")
def contact():
	return render_template("art.html")
	
@app.route("/photography")
def contact():
	return render_template("photography.html")

if __name__ == '__main__':
    app.run()
