from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from .models import User, Snippet
from . import db
from flask_login import current_user


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
            
from flask_bcrypt import check_password_hash           
class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')
    def validate(self):
        valid = super(LoginForm, self).validate()
        if not valid:
            return False

        user = User.query.filter_by(username=self.username.data).first()
        if not user or not check_password_hash(user.password, self.password.data):
            self.password.errors.append('Invalid username or password')
            return False

        return True

  


class SnippetForm(FlaskForm):
    title = StringField(validators=[InputRequired(), Length(min=1, max=80)], render_kw={"placeholder": "Insert Snippet Title!"})
    content = TextAreaField(validators=[InputRequired(), Length(min=1, max=1000)], render_kw={"placeholder": "//Insert Code!"})
    submit = SubmitField('Post')


class SearchForm(FlaskForm):
    title = StringField(validators=[InputRequired(), Length(min=1, max=80)], render_kw={"placeholder": "Search"})
    submit = SubmitField('Search')