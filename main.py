from flask import Flask, render_template

app = Flask(__name__)


def index():
    return render_template("index.html")


@app.route('/user/')
def user():
    list_fruits = [1, 1, 2]
    return render_template("user.html", list_fruits=list_fruits)
