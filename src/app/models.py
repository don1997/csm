from . import db
from flask_login import UserMixin
from datetime import datetime



snippet_tags = db.Table('snippet_tags',
    db.Column('snippet_id', db.Integer, db.ForeignKey('snippet.id'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True))
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    #unique=True: Two users cannot have same name
    username = db.Column(db.String(20), nullable=True, unique=True)
    password = db.Column(db.String(80), nullable=True)
    
    #Insert to include relationship User=Snippet
    snippets = db.relationship('Snippet', backref='author',lazy=True)


class Snippet(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=True)
    content = db.Column(db.Text, nullable=False)
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #userid
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_user_id') ,nullable=False)
    # Many-to-many relationship with Tag
    tags = db.relationship('Tag', secondary=snippet_tags, lazy='subquery',backref=db.backref('snippets', lazy=True))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)