from flask_migrate import Migrate

from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length, ValidationError

from flask_bcrypt import Bcrypt

from datetime import datetime


app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt=Bcrypt(app)
migrate = Migrate(app,db)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///database.db'

app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



"""
CLASSES
"""
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

""""
CLASSES
"""

"""
CLASS FORMS
"""
class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Register')
   
    #Handle case of duplicate names in form
    def validate_username(self, username):
        existing_user_username = User.query.filter_by(username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                "That username already exists. Please choose a different one")
            
class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')
 

# TODO
class SnippetForm(FlaskForm):
    
    snippet = TextAreaField(validators=[InputRequired()])

"""
CLASS FORMS
"""




"""
ROUTES
"""
@app.route('/')
def home():
    return render_template('home.html')



@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))


    return render_template('login.html', form=form)


@app.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout', methods=["GET","POST"])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))


    return render_template('register.html',form=form)

@app.route('/snippet/new', methods=['GET','POST'])
def new_snippet():
    
    form = SnippetForm()

    return render_template('new_snippet.html',form=form)
"""
ROUTES
"""
if __name__ == '__main__':
    app.run(debug=True)
