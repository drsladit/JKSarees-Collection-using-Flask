#location of this file  - myproject/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_login import LoginManager
#from flask_admin import Admin
#from flask_admin.contrib.sqla import ModelView
#from myproject.models import JKSarees


app = Flask(__name__)

#***********DATABSE SETUP********************************************************
app.config['SECRET_KEY'] = 'mysecretkey'
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABSE_URL", "sqlite:///data.db")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
migrate = Migrate(app,db)

#________________________________________________________________________________


#***********LOGIN Config********************************************************
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login'

#________________________________________________________________________________


# Buleprints registering
from myproject.core.view import core
from myproject.error_pages.handlers import error_pages
from myproject.users.view import users
from myproject.jksarees.view import jksarees

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(jksarees)

# Flask and Flask-SQLAlchemy initialization here

#admin = Admin(app)
#admin.add_view(ModelView(JKSarees, db.session))