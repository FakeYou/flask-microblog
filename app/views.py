from flask import render_template, flash, redirect
from flask.ext.login import login_user, logout_user, current_user

from app import app, db, login_manager
from .forms import LoginForm, RegisterForm, NewPostForm
from .models import User, Post

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/')
@app.route('/index')
def index():
    form = NewPostForm()

    posts = Post.query.order_by(Post.timestamp.desc()).all()
    
    return render_template('index.html', 
                           title='Home', 
                           form=form,
                           posts=posts)

@app.route('/newPost', methods=['POST'])
def newPost():
    form = NewPostForm()

    if current_user is None:
        return redirect('/index')

    if form.validate_on_submit():
        post = Post(current_user.id, form.body.data)
        db.session.add(post)
        db.session.commit()
        flash('Post added')
        return redirect('/index')

    return redirect('/index')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(form.nickname.data,
                    form.email.data,
                    form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Succesfully created user %s' % (user.nickname))
        return redirect('/login')

    return render_template('register.html',
                           title='Register new account',
                           form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        nickname = form.nickname.data
        password = form.password.data

        user = User.query.filter_by(nickname=nickname, password=password).first()
        if user is None:
            flash('Username or passowrd is invalid', 'error')
            return redirect('/login')

        login_user(user)
        flash('Logged in succesfully')
        return redirect('/index')

    return render_template('login.html',
                           title='Sign in',
                           form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/index')