""" Main app/routing file for Twitoff """

from flask import Flask, render_template
from .models import DB, User


# Creates application
def create_app():
    """ Creating and configuring an instance of the flask application """

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('base.html', title='home', users=User.query.all())

    return app





