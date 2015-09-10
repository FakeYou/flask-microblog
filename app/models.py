from app import db
from datetime import datetime

class User(db.Model):
    id            = db.Column(db.Integer, primary_key=True)
    nickname      = db.Column(db.String(64), index=True, unique=True)
    email         = db.Column(db.String(120), index=True, unique=True)
    password      = db.Column('password' , db.String(10))
    posts         = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, nickname, email, password):
        self.nickname = nickname
        self.password = password
        self.email    = email

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id        = db.Column(db.Integer, primary_key=True)
    body      = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id   = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, user_id, body):
        self.user_id   = user_id
        self.body      = body
        self.timestamp = datetime.utcnow()

    def __repr__(self):
        return '<Post %r>' % (self.body)