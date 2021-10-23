from flask import Flask, render_template
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
import news.news
from feedback.feedback import feedback


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)


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




app.register_blueprint(news, url_prefix="/news")
app.register_blueprint(feedback, url_prefix="/feedback")
