from flask_login import UserMixin
from liteversion import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
