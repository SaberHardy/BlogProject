from flask import Flask, render_template, flash, request, redirect, url_for
from models import UsersModel, db
from forms import UserForm, PasswordForm
from secret_staff import SECRET_STAFF
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='templates')  # static_folder='static')

# Create a Secret Key
app.config["SECRET_KEY"] = "mySecretKey"
# Sqlite DB
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
# My SqlDB
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://username:password@localhost/database_name"
app.config["SQLALCHEMY_DATABASE_URI"] = SECRET_STAFF

db.init_app(app)

migrate = Migrate(app, db)


@app.route('/user/add', methods=["Post", "Get"])
def add_user():
    name = None
    form = UserForm()

    if form.validate_on_submit():
        user = UsersModel.query.filter_by(email=form.email.data).first()
        if user is None:
            # Hash the password, and it's very important to remove the hashing algorithm "pbkdf2:sha256"
            hashed_pass = generate_password_hash(form.password_hash.data)

            # put data into database
            user = UsersModel(name=form.name.data,
                              email=form.email.data,
                              password_hash=hashed_pass)
            db.session.add(user)
            db.session.commit()

        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        # form.hashed_pass.data = ''
        flash("User added")

    all_users = UsersModel.query.order_by(UsersModel.date_added)
    return render_template("add_user.html",
                           form=form,
                           name=name,
                           all_users=all_users)


@app.route('/')
def all_users():
    get_users = UsersModel.query.all()
    return render_template("index.html", all_users=get_users)


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
        user_to_update.password1 = request.form['password1']

        try:
            db.session.commit()
            flash("User updated successfully!")
            return redirect(url_for('all_users'))
        except:
            flash("Error user")
            return render_template("update_user.html",
                                   form=form,
                                   user_to_update=user_to_update)
    else:
        form.name.data = user_to_update.name
        form.email.data = user_to_update.email
        form.email.password1 = user_to_update.password1
        return render_template("update_user.html",
                               form=form,
                               user_to_update=user_to_update)


@app.route('/delete/<int:id>/', methods=['POST', 'GET'])
def delete_user(id):
    user_to_delete = db.session.get(UsersModel, id)
    try:
        db.session.delete(user_to_delete)
        db.session.commit()
        flash("User deleted successfully")
        return redirect(url_for('all_users'))
    except:
        flash("Error user")

    return redirect(url_for('all_users'))


# Password Test
@app.route('/test_pass', methods=['GET', 'POST'])
def test_password():
    email = None
    password = None
    password_to_check = None
    passed = None
    form = PasswordForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password_hash.data

        form.email.data = ''
        form.password_hash.data = ''

        password_to_check = UsersModel.query.filter_by(email=email).first()
        passed = check_password_hash(password_to_check.password_hash, password)
        flash("The hash is correct!", "info")

        print(f"password_to_check {password_to_check.password_hash}")
        print(f"password {password}")

    return render_template('test_password.html',
                           form=form,
                           email=email,
                           password=password,
                           password_to_check=password_to_check,
                           passed=passed
                           )
