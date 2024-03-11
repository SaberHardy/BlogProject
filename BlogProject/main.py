from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')  # static_folder='static')

# Create a Secret Key
app.config["SECRET_KEY"] = "mySecretKey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db = SQLAlchemy(app)


class UsersModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name


# Create Form Class
class NameForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/user/<name>/')
def user(name):
    name = name
    return render_template("user.html", name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(error):
    return render_template('500.html'), 500


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("The form submitted successfully!", "info")

    return render_template('name.html', name=name, form=form)
