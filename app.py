# Pygments Stuff
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# Original app
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

# NEw app imports 
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column,DeclarativeBase


# Init Flask and Boostrap
def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

app = create_app()


# Create our db and its respective class
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

# SQLite configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String)

# Create tables in db
with app.app_context():
    db.create_all()
    
#original app
"""
@app.route("/")
def hello_world():
    return render_template('my_template.html')
"""
@app.route("/users")
# For annoying browser autocomplete!
@app.route("/users/")

def user_list():
    users = db.session.execute(db.select(User).order_by(User.id)).scalars()
    # Sanity check with template
    """
    for user in users:
        print(user.id, user.username, user.email)
    return "Check your console."
    """
    return render_template("user_list.html",users=users)

@app.route("/users/create", methods=["GET", "POST"])
def user_create():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "Username already exists!", 400

        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_detail", id=user.id))

    return render_template("user_create.html")


@app.route("/user/<int:id>")
def user_detail(id):
    user = db.get_or_404(User, id)
    return render_template("user_detail.html", user=user)

@app.route("/user/<int:id>/delete", methods=["GET", "POST"])
def user_delete(id):
    user = db.get_or_404(User, id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("user_list"))
#sanity check
@app.route("/test")
def test():
    code = 'print("Hello, World!")\ndef recur_factorial(n):\nif n == 1:\nreturn n\nelse:\nreturn n*recur_factorial(n-1)'
    highlighted_code = highlight(code, PythonLexer(), HtmlFormatter())
    return render_template('test.html', highlighted_code=highlighted_code)

"""
# Add snippet 
@app.route("/test/add")
def add():
    

    return render_template('add_snippet.html')

# Edit Snippet 
@app.route("/test/edit")
def add():
    

    return render_template('edit_snippet.html')

"""

@app.route("/", methods=["GET", "POST"])
def index():

    highlighted_code = None
    if request.method == "POST":
        code = request.form["code"]
        highlighted_code = highlight(code, PythonLexer(), HtmlFormatter())

    return render_template("index.html", highlighted_code=highlighted_code)

if __name__ == '__main__':
    app.run()
