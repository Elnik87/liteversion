from flask import Blueprint, render_template, request
from .models import News

news = Blueprint("news", __name__, template_folder="templates")


@news.route("/")
def newses():
    news = News.query.all()
    return render_template("news/news.html", news=news)


@news.route("/<slug>")
def news_detail(slug):
    news_detail = News.query.filter(News.slug == slug).first()
    return render_template("news/news_detail.html", news_detail=news_detail)
