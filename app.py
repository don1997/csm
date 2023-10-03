from flask import Flask

from flask_bootstrap import Bootstrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>I am using flask and bootstrap Hello!</p>"

if __name__ == '__main__':
    app.run()
