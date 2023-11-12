from . import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    #unique=True: Two users cannot have same name
    username = db.Column(db.String(20), nullable=True, unique=True)
    password = db.Column(db.String(80), nullable=True)
    
    #Insert to include relationship User=Snippet
    snippets = db.relationship('Snippet', backref='author',lazy=True)


class Snippet(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True, unique=True)
    content = db.Column(db.Text, nullable=False)
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #userid
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_user_id') ,nullable=False)
