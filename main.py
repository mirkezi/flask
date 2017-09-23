from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/forum')
def forum():
    return render_template('forum.html')


@app.route('/terminal')
def terminal():
    return render_template('terminal.html')

if __name__ == "__main__":
    app.run(debug=True)

