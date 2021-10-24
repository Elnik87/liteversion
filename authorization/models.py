from flask_login import UserMixin
from liteversion import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
