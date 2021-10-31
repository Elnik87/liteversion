from flask import Blueprint, render_template, request, flash, url_for
from flask_login import login_user, login_required, logout_user, current_user
from liteversion import bcrypt
from werkzeug.utils import redirect

from feedback.models import Feedback
from news.models import News
from liteversion import db
from .models import User
from news.forms import NewsForm, NewsUpdateForm
from news.utils import save_picture_news

admin = Blueprint("admin", __name__, template_folder="templates")


@admin.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        user = User.query.filter_by(login=login).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("admin.admins"))
            else:
                return redirect(url_for("admin.login"))
    else:
        return render_template("authorization/login.html")


@admin.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("/"))


@admin.route('/')
@login_required
def admins():
    news = News.query.order_by(News.date.desc()).all()
    feedbacks = Feedback.query.order_by(Feedback.date.desc()).all()
    return render_template("authorization/admin.html", news=news, feedbacks=feedbacks)


@admin.route('/create', methods=['POST', 'GET'])
@login_required
def create():
    form = NewsForm()
    if request.method == "POST":
        news = News(title=form.title.data, intro=form.intro.data, content=form.content.data)  # внимательнее на переменную
        picture_file = save_picture_news(form.picture.data)
        news.image = picture_file
        db.session.add(news)
        db.session.commit()
        flash("Новость опубликована")
        return redirect(url_for("admin.admins"))
    return render_template("authorization/create.html", form=form, legend="Новая новость")


@admin.route('/<slug>/news_update')
@login_required
def news_update(slug):
    news = News.query.filter(News.slug == slug).first()
    return render_template("authorization/news_update.html", news=news)


@admin.route('/<slug>/news_update_create', methods=["GET", "POST"])
@login_required
def news_update_create(slug):
    news = News.query.filter_by(slug=slug).first_or_404()
    form = NewsUpdateForm(obj=news)
    if request.method == "POST":
        news.title = form.title.data
        news.intro = form.intro.data
        news.content = form.content.data
        picture_file = save_picture_news(form.picture.data)
        news.image = picture_file
        db.session.add(news)
        db.session.commit()
        flash("Новость обновлена")
        return redirect("/")
    return render_template("authorization/news_update_create.html", news=news, form=form, legend="Новая новость")


@admin.route('/<slug>/news_delete')
@login_required
def news_delete(slug):
    news = News.query.filter_by(slug=slug).first()
    try:
        db.session.delete(news)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"Ошибка {e}"








