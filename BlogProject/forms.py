from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, EqualTo
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField


class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("User Name", validators=[DataRequired()])
    about_me = TextAreaField("About me")
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
    # content = StringField("Content", validators=[DataRequired()], widget=TextArea())
    content = CKEditorField('Content', validators=[DataRequired()])
    # author = StringField("Author")
    slug = StringField("Slug", validators=[DataRequired()])
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    username = StringField("User Name", validators=[DataRequired()])
    password = PasswordField("Enter your Password!", validators=[DataRequired()])
    submit = SubmitField("Submit")


class RegisterForm(FlaskForm):
    username = StringField("User Name", validators=[DataRequired()])
    password = PasswordField("Enter your Password!", validators=[DataRequired()])
    submit = SubmitField("Submit")


class SearchForm(FlaskForm):
    searched = StringField("Searched...", validators=[DataRequired()])
    submit = SubmitField("Submit")
