from flask import render_template

from liteversion import app
from news.views import news
from feedback.views import feedback
from authorization.views import admin


@app.route('/')
def index():
    return render_template("index.html", title="Неофициальный сайт 604 цСпН")


@app.route('/history')
def history():
    return render_template("history.html", title="История воинской части")


@app.route('/heroes')
def heroes():
    return render_template("heroes.html", title="Герои воинской части")


@app.route('/contract')
def contract():
    return render_template("contract.html", title="Служба по контракту")


@app.route('/beret')
def beret():
    return render_template("beret.html", title="Краповый берет")


app.register_blueprint(admin, url_prefix="/admin")
app.register_blueprint(news, url_prefix="/news")
app.register_blueprint(feedback, url_prefix="/feedback")
