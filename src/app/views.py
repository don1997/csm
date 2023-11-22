from flask import Blueprint, render_template, url_for, redirect, request, abort
from flask_login import login_user, login_required, logout_user, current_user
from . import db, bcrypt
from .models import User, Snippet
from .forms import LoginForm, RegisterForm, SnippetForm
from flask import flash


from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter


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


@main.route('/dashboard', defaults={'snippet_id': None})
@main.route('/dashboard/<int:snippet_id>')
@login_required
def dashboard(snippet_id):
    snippets = current_user.snippets
    selected_snippet = None
    highlighted_code = ""
    styles = ""
    if snippet_id:
        selected_snippet = Snippet.query.filter_by(id=snippet_id, user_id=current_user.id).first()
        if selected_snippet:
        
            highlighted_code = highlight(selected_snippet.content, PythonLexer(), HtmlFormatter())
    return render_template(
        'dashboard.html',
        snippets=snippets,
        selected_snippet=selected_snippet,
        highlighted_code=highlighted_code,
        styles=styles
    )
    
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

@main.route('/dashboard/new', methods=['GET','POST'])
@login_required
def new_snippet():
    
    form = SnippetForm()
    
    try:
        if form.validate_on_submit():
            existing_snippet = Snippet.query.filter_by(title=form.title.data, user_id=current_user.id).first()
            if existing_snippet:
                flash('Snippet title already exists. Enter unique title')
                return render_template('new_snippet.html',form=form)
            snippet = Snippet(title=form.title.data,content=form.content.data,author=current_user)
            db.session.add(snippet)
            db.session.commit()
            return redirect(url_for('main.dashboard'))
    except Exception as e:
        print(f"An error occurred: {e}")
        flash("An errror occurred while creating the snippet. PLease try again.", "error")

    return render_template('new_snippet.html',form=form)


@main.route('/dashboard/<int:id>/edit', methods=['GET','POST'])
@login_required
def edit_snippet(id):
    snippet = Snippet.query.get_or_404(id)
    
    if snippet.author != current_user:
        abort(403) 

    form = SnippetForm(obj=snippet)

    if form.validate_on_submit():
        # Check if there's another snippet with the same title, excluding the current snippet
        duplicate_snippet = Snippet.query.filter(Snippet.id != id, Snippet.title == form.title.data).first()
        
        if duplicate_snippet:
            flash('A snippet with this title already exists.', 'error')
            return render_template('edit_snippet.html', form=form)
            
        snippet.title = form.title.data
        snippet.content = form.content.data

        db.session.commit()
        return redirect(url_for('main.dashboard'))
    if request.method=='GET':
        form.title.data = snippet.title
        form.content.data = snippet.content
    return render_template('edit_snippet.html',form=form)


@main.route('/dashboard/<int:id>/delete', methods=['GET','POST'])
@login_required
def delete_snippet(id):
    try:
        snippet = Snippet.query.get_or_404(id)

        if snippet.author != current_user:
            abort(403) 
        db.session.delete(snippet)
        db.session.commit()
    
    except Exception as e:
        print(f"An error occurred: {e}")
        flash("An error occurred while deleting the snippet. PLease try again.", "error")

    return redirect(url_for('main.dashboard'))
    