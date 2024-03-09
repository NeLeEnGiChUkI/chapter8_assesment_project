from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegisterForm, AddproductForm


@app.route('/')
@app.route('/home')
def index():
    """Index URL"""
    return render_template('index.html', title='index')


@app.route('/about-me')
def about_me():
    """About Me URL"""
    return render_template('about-me.html', title='About Me')

@app.route('/login', methods=['GET', 'POST'])
@app.route('/login')
def login():
    """Login URL"""
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'you are requesting to login in{form.username.data}')
        return redirect (url_for('index'))
    return render_template('login.html', title='login', form=form)

@app.route('/register', methods=['GET', 'POST'])
@app.route('/register')
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'You have been successfuly registered{form.username.data}')
        return redirect (url_for('login'))
    return render_template('register.html', title='register', form=form)

@app.route('/addproduct', methods=['GET', 'POST'])
@app.route('/addproduct')
def add_product():
    """Add_product URL"""
    form = AddproductForm()
    if form.validate_on_submit():
        flash(f'You have been successfuly registered{form.username.data}')
        return redirect (url_for('login'))
    return render_template('addproduct.html', title='addproduct', form=form)

