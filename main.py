from flask import Flask, render_template
from news import News

app = Flask(__name__)

News = News()

class Login:

    __username: None
    __password: None

    def __init__(self, username, password):
        self.__username = username
        self.__password = password


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
