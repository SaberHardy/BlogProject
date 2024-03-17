from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from wtforms.widgets import TextArea


class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password_hash = PasswordField("Password",
                                  validators=[DataRequired(),
                                              EqualTo('password_hash2',
                                                      message='Passwords not matched')])

    password_hash2 = PasswordField("Confirm password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class PasswordForm(FlaskForm):
    email = StringField("What is your Email you want to check?", validators=[DataRequired()])
    password_hash = PasswordField("Enter your Password!", validators=[DataRequired()])

    # password_hash2 = PasswordField("Confirm password", validators=[DataRequired()])
    submit = SubmitField("Check Identity passwords !")


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = StringField("Content", validators=[DataRequired()], widget=TextArea())
    author = StringField("Author", validators=[DataRequired()])
    slug = StringField("Slug", validators=[DataRequired()])
    submit = SubmitField("Submit")
