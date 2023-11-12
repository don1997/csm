from flask import Blueprint, render_template, url_for, redirect, request, abort
from flask_login import login_user, login_required, logout_user, current_user
from . import db, bcrypt
from .models import User, Snippet
from .forms import LoginForm, RegisterForm, SnippetForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')



@main.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password,form.password.data):
                login_user(user)
                return redirect(url_for('main.dashboard'))


    return render_template('login.html', form=form)


@main.route('/dashboard',methods=['GET','POST'])
@login_required
def dashboard():
    #snippets = Snippet.query.all()
    snippets=current_user.snippets
    return render_template('dashboard.html',snippets=snippets)

@main.route('/logout', methods=["GET","POST"])
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))


    return render_template('register.html',form=form)

@main.route('/snippet/new', methods=['GET','POST'])
@login_required
def new_snippet():
    
    form = SnippetForm()
    
    if form.validate_on_submit():
        snippet = Snippet(title=form.title.data,content=form.content.data,author=current_user)
        db.session.add(snippet)
        db.session.commit()
        return redirect(url_for('main.dashboard'))

    return render_template('new_snippet.html',form=form)


@main.route('/snippet/<int:id>/edit', methods=['GET','POST'])
@login_required
def edit_snippet(id):
     
    snippet = Snippet.query.get_or_404(id)
    
    if snippet.author != current_user:
        abort(403) 

    form = SnippetForm(obj=snippet)

    if form.validate_on_submit():
        snippet.title = form.title.data
        snippet.content = form.content.data
        db.session.commit()
        return redirect(url_for('main.dashboard'))
    if request.method=='GET':
        form.title.data = snippet.title
        form.content.data = snippet.content
    return render_template('edit_snippet.html',form=form)


@main.route('/snippet/<int:id>/delete', methods=['GET','POST'])
@login_required
def delete_snippet(id):
  
    snippet = Snippet.query.get_or_404(id)

    if snippet.author != current_user:
        abort(403) 
    db.session.delete(snippet)
    db.session.commit()
    return redirect(url_for('main.dashboard'))

