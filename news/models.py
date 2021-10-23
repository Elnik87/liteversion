import re
from datetime import datetime
from route import db


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


def __init__(self, *args, **kwargs):
    super(News, self).__init__(*args, **kwargs)
    self.generate_slug()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(140), unique=True)
    content = db.Column(db.Text, nullable=False)
    # image = хочу добавить картинку, может видео итд, нашел в ютубе всякие руководства, но там хрен поймешь
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        super(News, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return "<News id: {}, title: {}".format(self.id, self.title)
