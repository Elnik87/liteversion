import re
from datetime import datetime
from liteversion import db
from transliterate import translit


def slugify(s):
    pattern = r'[^\w+]'
    a = translit(s, 'ru', reversed=True)
    return re.sub(pattern, '-', a)


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(140), unique=True)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(140), nullable=True, default="default.jpg")
    date = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Комментарии', backref='comments', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(News, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return "<News id: {}, title: {}".format(self.id, self.title)

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'), nullable=False)
