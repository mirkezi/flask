from flask import Flask, render_template
from news import News

app = Flask(__name__)

News = News()

import sqlite3

connection = sqlite3.connet('/userdb/login.db')

cursor = connection.cursor()


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/forum')
def forum():
    return render_template('forum.html')


@app.route('/news')
def terminal():
    return render_template('news.html', news=News)

if __name__ == "__main__":
    app.run(debug=True)
