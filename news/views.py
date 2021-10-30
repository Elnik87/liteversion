from flask import Blueprint, render_template, request, flash, url_for
from flask_login import current_user
from werkzeug.utils import redirect

from liteversion import db
from .forms import CommentForm
from .models import News, Comments

news = Blueprint("news", __name__, template_folder="templates")


@news.route("/")
def newses():
    news = News.query.all()
    return render_template("news/news.html", news=news)


@news.route("/<slug>")
def news_detail(slug):
    news_detail = News.query.filter(News.slug == slug).first()
    comments = Comments.query.filter(News.slug == slug).all()
    form = CommentForm()
    if form.validate_on_submit():
        comment = CommentForm(name=form.name.data, content=form.content.data, author=current_user)  # внимательнее на переменную
        db.session.add(comment)
        db.session.commit()
        flash("Комментарий опубликован")
        return redirect(url_for("/"))
    return render_template("news/news_detail.html", news_detail=news_detail, form=form, comments=comments)




