from flask import Flask, render_template

app = Flask(__name__)


def index():
    return render_template("index.html")


@app.route('/user/')
def user():
    list_fruits = [1, 1, 2]
    return render_template("user.html", list_fruits=list_fruits)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),  404

@app.errorhandler(500)
def page_not_found(error):
    return render_template('500.html'),  500

