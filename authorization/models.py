from flask_login import UserMixin
from liteversion import db, login_manager


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)


    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<User id: {}, login: {}".format(self.id, self.login)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
