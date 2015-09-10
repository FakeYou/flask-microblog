from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo, Length

class LoginForm(Form):
    nickname = StringField('nickname', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    remember_me = BooleanField('remember_me', default=False)

class RegisterForm(Form):
    nickname = StringField('nickname', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired(), Email()])
    password = PasswordField('password', validators=[InputRequired(), 
                                                     EqualTo('confirm', message='Password must match')])
    confirm = PasswordField('confirm password')

class NewPostForm(Form):
    body = StringField('body', validators=[InputRequired(), Length(max=140)])