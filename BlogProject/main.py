from flask import Flask, render_template, flash, request
from models import UsersModel, db
from forms import UserForm
from secret_staff import SECRET_STAFF

app = Flask(__name__, template_folder='templates')  # static_folder='static')

# Create a Secret Key
app.config["SECRET_KEY"] = "mySecretKey"
# Sqlite DB
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
# My SqlDB
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://username:password@localhost/database_name"
app.config["SQLALCHEMY_DATABASE_URI"] = SECRET_STAFF

db.init_app(app)


@app.route('/user/add', methods=["Post", "Get"])
def add_user():
    name = None
    form = UserForm()

    if form.validate_on_submit():
        user = UsersModel.query.filter_by(email=form.email.data).first()
        if user is None:
            user = UsersModel(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()

        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash("User added")

    all_users = UsersModel.query.order_by(UsersModel.date_added)
    return render_template("add_user.html",
                           form=form,
                           name=name,
                           all_users=all_users)


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
    form = UserForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("The form submitted successfully!", "info")

    return render_template('name.html', name=name, form=form)


@app.route('/update/<int:id>/', methods=['POST', 'GET'])
def update_user(id):
    form = UserForm(request.form)
    user_to_update = UsersModel.query.get_or_404(id)
    if request.method == 'POST':
        user_to_update.name = request.form['name']
        user_to_update.email = request.form['email']

        try:
            db.session.commit()
            flash("User updated successfully!")
            return render_template("update_user.html",
                                   form=form,
                                   user_to_update=user_to_update)
        except:
            flash("Error user")
            return render_template("update_user.html",
                                   form=form,
                                   user_to_update=user_to_update)
    else:
        return render_template("update_user.html",
                               form=form,
                               user_to_update=user_to_update)
