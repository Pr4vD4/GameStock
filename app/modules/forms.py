from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, EmailField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    input_username = StringField('inputUsername', validators=[DataRequired()])
    input_password = PasswordField('inputPassword', validators=[DataRequired()])
    input_remember_me = BooleanField('remember_me', default=False)

class RegisterForm(FlaskForm):
    input_email = EmailField('inputEmail', validators=[DataRequired()])
    input_username = StringField('inputUsername', validators=[DataRequired()])
    input_password = PasswordField('inputPassword', validators=[DataRequired()])
    input_password_confirm = PasswordField('inputPasswordConfirm', validators=[DataRequired()])
    input_mailing = BooleanField('mailing', default=True)