from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from config import Configuration
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "admin.login"
# db.create_all() # Не уверен, но может так лучше сделать БД, чем через консоль

from liteversion import views
