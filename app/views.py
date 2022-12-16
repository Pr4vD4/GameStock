from app import app
from flask import render_template, flash ,redirect

from .modules.bg_counter import *
from .modules.forms import LoginForm, RegisterForm

from config import *


@app.route('/')
@app.route('/#')
def index():
    data = {
        'title': 'Game Title',
        'text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Assumenda cum cumque dolor explicabo hic id illum incidunt, minima possimus quidem quo repellendus sunt tempora veritatis.',
        'image': 'https://thelastgame.ru/wp-content/uploads/2017/10/header-92-520x245.jpg'
    }
    return render_template('pages/index.html', title=WEBSITE_NAME, bg=bg_counter(), page='home', data=data)


@app.route('/game/<id>')
def game(id):
    return render_template('pages/game.html', title=WEBSITE_NAME, bg=bg_counter(), page='game', id=id)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegisterForm()
    if form.validate_on_submit():
        print('hello')
        flash('Register requested Email="' + str(form.input_email.data) +'", Username="' + str(form.input_username.data) + '", Password="' + str(form.input_password.data)+'", PasswordConfirmtion="' + str(form.input_password_confirm.data)+'", Mailing="'+str(form.input_mailing.data)+'"')
        return redirect('/')
    return render_template('pages/register.html', title=WEBSITE_NAME, bg=bg_counter(), page='login', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested Username="' + str(form.input_username.data) + '", Password=' + str(form.input_password.data))
        return redirect('/')
    return render_template('pages/login.html', title=WEBSITE_NAME, bg=bg_counter(), page='login', form=form)


@app.errorhandler(404)
def not_found(error):
    return render_template('pages/error_page.html', error=error, bg=bg_counter())
