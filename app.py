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
    'comment':'sqlite:///comment.db',
    'vote':'sqlite:///vote.db'

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

# database models

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(20),nullable=False)
    email=db.Column(db.String(120),nullable=False)
    password=db.Column(db.String(60),nullable=False)
    colleague=db.column(db.String(100),default=" ")

    def __repr__(self):
        return f"User('{self.id}','{self.username}','{self.email}','{self.colleague}')"


# post table

class Posts(db.Model):
    __bind_key__='posts'
    uid=db.Column(db.Integer)
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(500),primary_key=True)

#comment table
class Comments(db.Model):
    __bind_key__='comment'
    id=db.Column(db.Integer,primary_key=True)
    uid=db.Column(db.Integer)
    pid=db.Column(db.Integer)
    com=db.Column(db.String(150),nullable=False)

#votetable
# class Votes(db.Model):
#     __bind_key__='vote'
#     uid=db.Column(db.Integer)
#     pid=db.Column(db.Integer)
#     up=db.Column(db.Integer,)


from routes import *

if __name__=="main":
    app.run(debug=True)


