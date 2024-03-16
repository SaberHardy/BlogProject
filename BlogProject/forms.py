from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class UserForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password_hash = PasswordField("Password",
                                  validators=[DataRequired(),
                                              EqualTo('password_hash2',
                                                      message='Passwords not matched')])

    password_hash2 = PasswordField("Confirm password", validators=[DataRequired()])
    submit = SubmitField("Submit")
