import os
basedir = os.path.abspath(os.path.dirname(__file__))

print(basedir)

WTF_CSRF_ENABLED = True
SECRET_KEY = 'nsssssssss789rhga9ohOAHY789sd hAsdg9d& B(ASH&*DogH789yasdtOAI7fga'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')