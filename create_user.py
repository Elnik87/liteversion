from liteversion import app, bcrypt
from authorization.models import User, db


def main():
    with app.app_context():
        db.metadata.create_all(db.engine)  # подключение к БД
        user = User(login="Elnik", password=bcrypt.generate_password_hash(password="12345").decode("utf-8"))  # добавляем пользователя, декод добавлять всегда
        db.session.add(user)
        db.session.commit()

if __name__ == '__main__':
    main()
