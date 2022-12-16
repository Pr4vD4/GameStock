from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    input_username = StringField('inputUsername', validators=[DataRequired()])
    input_password = PasswordField('inputPassword', validators=[DataRequired()])
    input_remember_me = BooleanField('remember_me', default=False)
