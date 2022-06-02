import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager,UserMixin
from flask_restful import Api,Resource
import os
from werkzeug.utils import secure_filename

app=Flask(__name__)
app.config['SECRET_KEY']='8efde650d0e727ef697bb75adb2a114a'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///user.db'
app.config['SQLALCHEMY_BINDS']={
    'posts':'sqlite:///posts.db',
    'comment':'sqlite:///comment.db'

}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category='info'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))