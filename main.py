from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('homepage.html')


@app.route('/profile')
def profile():
    return

if __name__ == "__main__":
    app.run(debug=True)

