from flask import Flask
from flask_login import LoginManager

from config import Configuration
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.init_app(app)
# db.create_all() # Не уверен, но может так лучше сделать БД, чем через консоль

from liteversion import views
